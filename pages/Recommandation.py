import streamlit as st
import pandas as pd
import json

with open('output/merged_result.json', 'r') as file:
    data = json.load(file)

restaurants = pd.DataFrame(data)

# Configurer la page Streamlit
st.title("Recommandations de Restaurants Végans à Paris")
st.markdown("Trouvez les meilleurs restaurants végans selon vos préférences.")