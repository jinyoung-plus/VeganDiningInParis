import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

from folium.plugins import MarkerCluster

st.set_page_config(page_title="Home", layout="centered")

st.title("Welcome to the Recommendation App")
st.markdown("""
Welcome to your guide to vegan restaurants in Paris 🌱. 
- Explore restaurants by rating.
- View locations on an interactive map.
- Check out some interesting statistics.
Use the menu on the left to navigate between pages.
""")

st.snow()

st.divider()
st.page_link("app.py", label="Home", icon="🌱")
st.page_link("pages/Research.py", label="Restaurant Recommender", icon="1️⃣")
st.page_link("pages/Favorite.py", label="Favorite", icon="⭐")
st.page_link("pages/Statistics.py", label="Statisitcs", icon="%")
st.divider()

