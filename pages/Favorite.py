import streamlit as st
import folium
from streamlit_folium import st_folium

# Initialize session state for favorites
if "favorites" not in st.session_state:
    st.session_state.favorites = []

# Function to remove a favorite
def remove_favorite(restaurant_name):
    st.session_state.favorites = [fav for fav in st.session_state.favorites if fav['Name'] != restaurant_name]

# Page Title
st.set_page_config(page_title="Favorites", layout="wide")
st.title("Your Favorite Restaurants")

# Display favorites
if st.session_state.favorites:
    st.write("### Here are your favorite restaurants:")

    # Create a map to display favorite locations
    map_favorites = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

    for favorite in st.session_state.favorites:
        # Display detailed information for each favorite
        st.markdown(f"""
        <div style="border:1px solid #ddd; border-radius:8px; padding:10px; margin-bottom:10px;">
            <h3>{favorite['Name']}</h3>
            <p><strong>Address:</strong> {favorite['Address']}</p>
            <p><strong>Rating:</strong> {favorite['Rating']} | <strong>Reviews:</strong> {favorite['Reviews_Count']}</p>
            <p><strong>Customer Reviews:</strong></p>
            <ul>
                {''.join([f'<li>{review}</li>' for review in favorite['Reviews'][:2]])}
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # Add a button to remove the favorite
        if st.button(f"❌ Remove {favorite['Name']} from Favorites", key=f"remove-{favorite['Name']}"):
            remove_favorite(favorite['Name'])

        # Add marker to the map
        folium.Marker(
            location=[favorite['Location']['latitude'], favorite['Location']['longitude']],
            popup=f"{favorite['Name']}<br>Rating: {favorite['Rating']}<br>Reviews: {favorite['Reviews_Count']}",
            tooltip=favorite['Name']
        ).add_to(map_favorites)

    # Display the map
    st.write("### Map of Favorite Restaurants")
    st_folium(map_favorites, width=700, height=500)

else:
    st.write("You haven't added any favorites yet. Go back and add some!")
