import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Favorite", layout="wide")
st.title("Restaurant Favorite")
# Section des favoris
st.write("### Your Favorites")
if st.session_state.favorites:
    for favorite in st.session_state.favorites:
        st.write(f"- {favorite}")
else:
    st.write("No favorites yet. Add some!")