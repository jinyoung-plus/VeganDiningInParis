import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

st.set_page_config(
    page_title="Vegan recommendation",
    layout="wide"
)


# Streamlit 제목
st.title("Paris Landmark Map Viewer")



import re
import os

# Disable GPU
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# Set file paths
merged_data_file = '/content/drive/MyDrive/0_2024DIA/Webscraping/p1/output/merged_data_en_cleaned.json'
word2vec_embeddings_file = '/content/drive/MyDrive/0_2024DIA/Webscraping/p1/output/word2vec_embeddings.npy'
bert_embeddings_file = '/content/drive/MyDrive/0_2024DIA/Webscraping/p1/output/bert_embeddings.npy'

# Load data and embeddings
@st.cache_data
def load_data():
    data = pd.read_json(merged_data_file)
    return data

@st.cache_resource
def load_embeddings():
    word2vec_embeddings = np.load(word2vec_embeddings_file)
    bert_embeddings = np.load(bert_embeddings_file)
    return word2vec_embeddings, bert_embeddings

# Load data
data = load_data()
word2vec_embeddings, bert_embeddings = load_embeddings()

# Streamlit app title
st.title("Paris Vegan Restaurant Recommender")

# Add CSS styles
st.markdown("""
    <style>
    .review-card {
        border: 1px solid #ccc; 
        border-radius: 10px; 
        padding: 10px; 
        margin: 10px 0; 
        background-color: #f9f9f9; 
        color: black;
        max-height: 300px;
        overflow-y: auto;
    }
    .review-card h3 {
        color: black;
        margin-bottom: 5px;
    }
    .review-card p {
        margin: 0;
        color: black;
    }
    .customer-reviews {
        max-height: 100px;
        overflow-y: auto;
        margin-top: 10px;
        padding: 5px;
        background: #e9ecef;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize user input
if "results" not in st.session_state:
    st.session_state.results = None

# User input form
with st.form(key='search_form'):
    user_query = st.text_input("Enter your search query (e.g., cozy vegan desserts):", "cozy vegan desserts")
    user_rating_threshold = st.slider("Minimum Rating", 0.0, 5.0, 4.0, 0.1)
    user_min_reviews = st.number_input("Minimum number of reviews", min_value=0, value=10, step=5)

    # Select districts (1-20)
    st.write("Select your preferred Paris Districts:")
    district_rows = st.columns(2)
    districts_col1 = district_rows[0].multiselect("1-10", options=[i for i in range(1, 11)], default=[1, 3, 5])
    districts_col2 = district_rows[1].multiselect("11-20", options=[i for i in range(11, 21)], default=[12, 14, 16])
    user_districts = districts_col1 + districts_col2

    sort_option = st.selectbox("Sort by", options=["Final Score", "Rating", "Reviews_Count"])
    submit_button = st.form_submit_button(label='Search')

if submit_button:
    # Query preprocessing
    def preprocess_query(query):
        query = query.lower().strip()
        query = re.sub(r"[^\w\s]", "", query)
        return query

    user_query = preprocess_query(user_query)

    # Set weights
    alpha = 0.5  # BM25 weight
    beta = 0.3   # BERT weight
    gamma = 0.2  # Rating weight

    # Preprocess 'Rating' and 'Reviews_Count'
    data['Rating'] = pd.to_numeric(data['Rating'], errors='coerce').fillna(3.0)
    data['Reviews_Count'] = pd.to_numeric(data['Reviews_Count'], errors='coerce').fillna(0).astype(int)

    # Extract district from address
    def extract_district(address):
        match = re.search(r'750(\d{2})', address)
        if match:
            return int(match.group(1))
        return None

    data['District'] = data['Address'].apply(extract_district)

    # Calculate BM25 score
    tokenized_corpus = [doc.split() for doc in data['Merged_data']]
    bm25 = BM25Okapi(tokenized_corpus)
    tokenized_query = user_query.split()
    bm25_scores = bm25.get_scores(tokenized_query)

    # Calculate BERT similarity
    bert_model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = bert_model.encode(user_query).reshape(1, -1)
    bert_similarities = cosine_similarity(query_embedding, bert_embeddings).flatten()

    # Integrate scores
    data['BM25_Score'] = bm25_scores
    data['BERT_Similarity'] = bert_similarities
    data['Final_Score'] = (
        alpha * data['BM25_Score'] +
        beta * data['BERT_Similarity'] +
        gamma * data['Rating']
    )

    # Filtering
    filtered_data = data[
        (data['Rating'] >= user_rating_threshold) &
        (data['Reviews_Count'] >= user_min_reviews) &
        (data['District'].isin(user_districts))
    ]

    # Determine sorting column
    sort_option_column = {"Final Score": "Final_Score", "Rating": "Rating", "Reviews_Count": "Reviews_Count"}[sort_option]
    top_recommendations = filtered_data.sort_values(by=sort_option_column, ascending=False).head(10)

    # Save results
    st.session_state.results = top_recommendations

# Display results
if st.session_state.results is not None:
    st.write("### Top Recommendations")
    for _, row in st.session_state.results.iterrows():
        # Check and process reviews
        customer_reviews = ""
        if isinstance(row['Reviews'], list) and len(row['Reviews']) > 0:  # Check if reviews exist
            # Create a properly formatted string for reviews
            customer_reviews_list = [f"- {review}" for review in row['Reviews'][:3]]  # Limit to 3 reviews
            customer_reviews = "<br>".join(customer_reviews_list)  # Join reviews with a line break for display
        else:
            customer_reviews = "No reviews available for this restaurant."

        # Render HTML for the recommendation card
        st.markdown(f"""
        <div class="review-card">
            <h3>{row['Name']}</h3>
            <p><strong>Address:</strong> {row['Address']}</p>
            <p><strong>Rating:</strong> {row['Rating']} | <strong>Reviews:</strong> {row['Reviews_Count']}</p>
            <p><strong>Matching Score:</strong> {row['Final_Score']:.2f}</p>
            <div class="customer-reviews">
                <strong>Customer Reviews:</strong>
                <p>{customer_reviews}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Display the map with recommendations
    st.write("### Map of Recommendations")
    paris_map = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

    for _, row in st.session_state.results.iterrows():
        folium.Marker(
            location=[row['Location']['latitude'], row['Location']['longitude']],
            popup=f"{row['Name']}<br>Rating: {row['Rating']}<br>Reviews: {row['Reviews_Count']}",
            tooltip=row['Name']
        ).add_to(paris_map)

    st_folium(paris_map, width=700, height=500)
