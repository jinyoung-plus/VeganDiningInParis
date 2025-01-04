import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configure the Streamlit page
st.set_page_config(page_title="Restaurant Statistics", layout="wide")
st.title("Restaurant Statistics")

# Load the data
data_path = "output/merged_data_en_cleaned.json"
data = pd.read_json(data_path)

# Clean the data
data['Rating'] = pd.to_numeric(data['Rating'], errors='coerce').fillna(0)
data['Reviews_Count'] = pd.to_numeric(data['Reviews_Count'], errors='coerce').fillna(0)

# Extract latitude and longitude if available
def extract_coordinates(location):
    if isinstance(location, dict):
        return location.get('latitude', None), location.get('longitude', None)
    return None, None

data['Latitude'], data['Longitude'] = zip(*data['Location'].apply(extract_coordinates))
st.divider()
# Display global statistics
st.markdown("## Global Statistics")
st.write(f"Total number of restaurants: {len(data)}")
st.write(f"Average rating: {data['Rating'].mean():.2f}")
st.write(f"Average number of reviews: {data['Reviews_Count'].mean():.2f}")
st.divider()
# Histogram of ratings
st.markdown("### Distribution of Restaurant Ratings")
hist_fig = px.histogram(
    data, 
    x="Rating", 
    nbins=10, 
    title="Distribution of Ratings", 
    labels={"Rating": "Rating"},
    color_discrete_sequence=["skyblue"]
)
hist_fig.update_layout(yaxis_title="Number of restaurants")
st.plotly_chart(hist_fig)
st.divider()
# Top 10 restaurants by number of reviews
st.markdown("### Top 10 Restaurants by Number of Reviews")
top_reviews = data.nlargest(10, 'Reviews_Count')
bar_fig = px.bar(
    top_reviews, 
    x="Reviews_Count", 
    y="Name", 
    orientation="h", 
    title="Top 10 Restaurants by Number of Reviews", 
    labels={"Reviews_Count": "Number of reviews", "Name": "Restaurant"},
    color_discrete_sequence=px.colors.sequential.Viridis
)
st.plotly_chart(bar_fig)
st.divider()
# Map of restaurants
st.markdown("### Restaurant Locations")
map_fig = px.scatter_mapbox(
    data.dropna(subset=['Latitude', 'Longitude']), 
    lat="Latitude", 
    lon="Longitude", 
    hover_name="Name", 
    hover_data={"Rating": True, "Reviews_Count": True},
    color="Rating",
    color_continuous_scale=px.colors.sequential.Viridis,
    title="Map of Restaurants"
)
map_fig.update_layout(
    mapbox_style="open-street-map",
    margin={"r":0,"t":0,"l":0,"b":0}
)
st.plotly_chart(map_fig)
st.divider()
