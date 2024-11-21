# VeganDiningInParis 🍽️🌱

A **Streamlit-based recommendation system** for **vegan travelers in Paris**, providing personalized vegan restaurant recommendations using advanced text analysis and Google Maps integration.

---

## 📖 Project Overview

### **Purpose**
The goal of this project is to help vegan travelers find the best restaurants in Paris by leveraging data from **Yelp** and **Google Maps**. Using a **BM25-based recommendation system**, we identify the most relevant restaurants based on user preferences and reviews.

### **Key Features**
- **Personalized Search**: Input a keyword (e.g., "burger", "romantic dinner") to find the most relevant vegan restaurants in Paris.
- **Integrated Google Maps**: View restaurant locations directly on an interactive map with markers.
- **Detailed Restaurant Information**: Access ratings, review counts, categories, and user reviews for each restaurant.
- **Multi-Source Data**: Combined information from Yelp and Google Maps to provide accurate and comprehensive recommendations.

---

## 🛠️ Technologies Used

### **Frontend & Visualization**
- [Streamlit](https://streamlit.io): Interactive user interface and web app deployment.
- [Folium](https://python-visualization.github.io/folium/): Map visualization for displaying restaurant locations.

### **Backend & Processing**
- [BM25](https://github.com/dorianbrown/rank_bm25): A ranking algorithm for personalized search results.
- [Google Maps API](https://developers.google.com/maps): Address geocoding and map integration.
- [Selenium](https://www.selenium.dev/): Web scraping for dynamic pages.
- [Pandas](https://pandas.pydata.org/): Data manipulation and analysis.
- [OpenAI GPT API](https://platform.openai.com/): Keyword generation for enhancing restaurant recommendations.

### **Data Sources**
1. **Yelp**: Restaurant names, categories, addresses, ratings, and reviews.
2. **Google Maps**: Restaurant names, addresses, ratings, review counts, and user reviews.

---

## 🚀 How to Use

### **1. Prerequisites**
- Python 3.8+ installed.
- Install required Python packages:
  ```bash
  pip install -r requirements.txt

### **2. Run the Application**

#### **Clone the repository**:
```bash
 git clone https://github.com/jinyoung-plus/VeganDiningInParis.git
 cd VeganDiningInParis
```
#### **Start the Streamlit application**:
```bash
 streamlit run app.py
 ```
#### **Open your browser at http://localhost:8501.**

### **3. Search for Restaurants**
- Enter a keyword in the search bar (e.g., "desserts", "healthy").
- View the top recommended vegan restaurants.
- Check restaurant locations and details directly on the interactive map.

---

## 📊 Data Pipeline
### **1. Data Collection**
- Yelp:
  - Web scraping with Selenium to collect restaurant details (name, category, address, rating, reviews).
- Google Maps:
  - SERP API to extract restaurant details and reviews.

### **2. Data Processing**
- Data Cleaning:
  - Merge Yelp and Google Maps data, handle duplicates, and normalize information.
- Text Preprocessing:
  - Combine reviews and categories for each restaurant into a unified text field.
### **3. Recommendation Engine**
- BM25 Algorithm:
  - Ranks restaurants based on the relevance of user input to restaurant data.
### **4. Map Integration**
- Google Maps API:
  - Convert addresses to geographic coordinates.
  - Display restaurant markers on an interactive map.

---

## 🎨 Application Features
### **Search Results
- Displays a ranked list of vegan restaurants in Paris based on user input.
- Shows restaurant names, ratings, review counts, and a snippet of user reviews.
### **Interactive Map
- Visualizes restaurant locations in Paris.
- Clickable markers for restaurant details.
### **Restaurant Details
- Comprehensive information about each restaurant:
  - Categories (e.g., Vegan, French Cuisine)
  - Average rating
  - Total reviews
  - User reviews (up to 5 recent ones)

---

## 🌟 Future Improvements
- Enhanced Filters:
  - Add filters for price range, proximity, or opening hours.
- User Reviews Analysis:
  - Perform sentiment analysis to highlight restaurants with consistently positive feedback.
- Multi-Language Support:
  - Translate restaurant information for non-English-speaking users.
- Real-Time Updates:
  - Use APIs to fetch the latest data dynamically.
  
---

## 👥 Team Collaboration
### **Contributors
Jinyoung KO: Data scraping and analysis, BM25 implementation.
Sainan BI: Streamlit UI and Google Maps integration, Keyword generation and data cleaning.

---

## 📜 License
This project is licensed under the MIT License.
  
---

## 📬 Contact
If you have any questions or feedback, feel free to reach out:

- Email: jinyoung.ko@edu.devinci.fr
- GitHub: jinyoung-plus
