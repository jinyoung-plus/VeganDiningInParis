import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

from folium.plugins import MarkerCluster

st.set_page_config(page_title="Home", layout="centered")

st.title("Bienvenue dans l'Application de Recommandation")
st.markdown("""
Bienvenue dans votre guide des restaurants végans à Paris 🌱. 
- Explorez les restaurants par classement.
- Visualisez les localisations sur une carte interactive.
- Consultez des statistiques intéressantes.
Utilisez le menu à gauche pour naviguer entre les pages.
""")

st.snow()

st.page_link("app.py", label="Home", icon="🌱")
st.page_link("pages/Research.py", label="Restaurant Recommender", icon="1️⃣")
st.page_link("pages/Favorite.py", label="Favorite", icon="⭐")


