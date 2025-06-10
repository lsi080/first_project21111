pip install streamlit folium geopy requests
import streamlit as st
import folium
from folium import Marker
from streamlit_folium import st_folium
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import requests

# 주소 -> 좌표 변환 함수
def geocode_address(address):
    geolocator = Nominatim(user_agent="accessibility-app")
    location = geolocator.geocode(address)
    return (location.latitude, location.longitude) if location else (None, None)

# 예시: 도서관 위치 데이터를 공공 API에서 가져오는 함수 (간단히 고정된 예시로 대체 가능)
def get_public_facilities(facility_type="도서관"):
    # 실제 서비스에서는 OpenAPI 요청을 넣을 수 있습니다.
    # 여기선 예시로 고정된 시설 데이터를 사용합니다.
    return [
        {"name": "서울시립도서관", "lat": 37.5665, "lon": 126.9780},
        {"name": "강남도서관", "lat": 37.4955, "lon": 127.0622},
        {"name": "마포중앙도서관", "lat": 37.5637, "lon": 126.9084},
    ]

# 거리 기반 접근성 지수 계산 (예: 가까울수록 지수 ↑)
def calculate_accessibility(distance_km):
    return round(max(0, 100 - distance_km * 10), 2)  # 단순 모델: 1km마다 10점 감소

st.title("🏙️ 도시 내 공공시설 접근성 분석 앱")
st.markdown("건축 + 데이터 분석 기반 접근성 시각화")

# 사용자 입력
address = st.text_input("🏠 거주지 주소를 입력하세요", "서울특별시 중구 세종대로 110")
facility_type = st.selectbox("🏢 원하는 공공시설 종류를 선택하세요", ["도서관", "병원", "공원"])

if address:
    user_lat, user_lon = geocode_address(address)

    if user_lat and user_lon:
        st.success(f"입력한 주소의 위치: ({user_lat:.4f}, {user_lon:.4f})")

        facilities = get_public_facilities(facility_type)
        m = folium.Map(location=[user_lat, user_lon], zoom_start=12)

        folium.Marker([user_lat, user_lon], tooltip="사용자 위치", icon=folium.Icon(color='blue')).add_to(m)

        for f in facilities:
            facility_loc = (f["lat"], f["lon"])
            distance_km = geodesic((user_lat, user_lon), facility_loc).km
            accessibility_score = calculate_accessibility(distance_km)

            popup_text = f"{f['name']}<br>거리: {distance_km:.2f}km<br>접근성 지수: {accessibility_score}"
            folium.Marker(
                location=facility_loc,
                popup=popup_text,
                tooltip=f["name"],
                icon=folium.Icon(color="green" if accessibility_score > 70 else "red")
            ).add_to(m)

        st.markdown("### 🗺️ 지도 시각화")
        st_folium(m, width=700, height=500)
    else:
        st.error("주소를 찾을 수 없습니다. 다시 입력해 주세요.")
