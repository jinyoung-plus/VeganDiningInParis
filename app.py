import streamlit as st
import pandas as pd
import folium
from geopy.geocoders import GoogleV3
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

st.set_page_config(
    page_title="Vegan recommendation",
    layout="wide"
)


# Streamlit 제목
st.title("Paris Landmark Map Viewer")

"""
# Google Maps API 키 설정
API_KEY = "AIzaSyDza7pLB-ddE2XEHhX3fJkJ_XlaSUqg3Gs"

# Google Geocoding 객체 생성
geolocator = GoogleV3(api_key=API_KEY)

# 주소를 위도와 경도로 변환하는 함수
def geocode_address(name, address):
    try:
        full_address = f"{name}, {address}"
        location = geolocator.geocode(full_address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except Exception:
        return None, None

# CSV 파일 읽기
csv_file_path = "address.csv"  # address.csv 파일이 같은 디렉토리에 있어야 합니다
with open(csv_file_path, "r") as file:
    raw_data = file.readlines()

# 첫 번째 행 제거 (헤더)
raw_data = raw_data[1:]

# 데이터를 파싱하여 DataFrame으로 변환
parsed_data = []
for row in raw_data:
    parts = row.split(",", 1)
    name = parts[0].strip()
    address = parts[1].strip() if len(parts) > 1 else ""
    parsed_data.append([name, address])

data = pd.DataFrame(parsed_data, columns=["name", "address"])

# 주소를 위도와 경도로 변환
data[['latitude', 'longitude']] = data.apply(
    lambda row: pd.Series(geocode_address(row['name'], row['address'])), axis=1
)

# 유효 데이터 필터링
valid_data = data.dropna(subset=['latitude', 'longitude'])

# 지도 생성
paris_coordinates = [48.8566, 2.3522]
m = folium.Map(location=paris_coordinates, zoom_start=13)

# 마커 클러스터 추가
marker_cluster = MarkerCluster().add_to(m)

# 데이터에서 위치를 읽어 클러스터에 추가
for i, row in valid_data.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"<b>{row['name']}</b><br>{row['address']}",
        tooltip=f"{row['name']}",
        icon=folium.Icon(color='red', icon='info-sign')  # 마커 색상을 빨간색으로 설정
    ).add_to(marker_cluster)

# 지도 렌더링
st.write("Explore the landmarks of Paris:")
st_folium(m, width=725, height=500)
"""