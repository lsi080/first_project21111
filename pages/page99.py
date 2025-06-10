# 필요한 라이브러리 임포트
import streamlit as st                      # Streamlit 웹앱 프레임워크
import folium                               # 지도 시각화를 위한 라이브러리
from streamlit_folium import st_folium      # Streamlit에 folium 지도를 띄우기 위한 모듈
from geopy.geocoders import Nominatim       # 주소를 위도/경도로 바꾸는 지오코딩 도구
from geopy.distance import geodesic         # 두 지점 사이 거리 계산

# -------------------------------
# 페이지 기본 설정
st.set_page_config(page_title="도시 공공시설 접근성 분석", layout="wide")
st.title("🏙️ 도시 내 공공시설 접근성 분석 앱")
st.markdown("건축 + 데이터 분석 기반 접근성 시각화 웹앱입니다.")

# -------------------------------
# 주소를 위도, 경도로 변환하는 함수
def geocode_address(address):
    geolocator = Nominatim(user_agent="accessibility-app")  # 사용자 정의 이름
    location = geolocator.geocode(address)                   # 주소를 위도/경도로 변환
    return (location.latitude, location.longitude) if location else (None, None)

# -------------------------------
# 시설 종류에 따라 예시 위치 데이터를 반환하는 함수
def get_facilities(facility_type):
    if facility_type == "도서관":
        return [
            {"name": "서울도서관", "lat": 37.5665, "lon": 126.9780},
            {"name": "강남도서관", "lat": 37.4955, "lon": 127.0622},
            {"name": "마포중앙도서관", "lat": 37.5637, "lon": 126.9084},
        ]
    elif facility_type == "병원":
        return [
            {"name": "서울대병원", "lat": 37.5796, "lon": 126.9979},
            {"name": "삼성서울병원", "lat": 37.4894, "lon": 127.0850},
            {"name": "강북삼성병원", "lat": 37.5670, "lon": 126.9660},
        ]
    elif facility_type == "공원":
        return [
            {"name": "서울숲", "lat": 37.5446, "lon": 127.0375},
            {"name": "남산공원", "lat": 37.5512, "lon": 126.9882},
            {"name": "월드컵공원", "lat": 37.5684, "lon": 126.8963},
        ]
    return []

# -------------------------------
# 거리 기반 접근성 점수를 계산하는 함수
def calculate_accessibility(distance_km):
    # 거리(km)가 멀수록 점수가 낮아짐 (100점 만점)
    return round(max(0, 100 - distance_km * 10), 2)

# -------------------------------
# 사용자 입력 받기
address = st.text_input("🏠 거주지 주소를 입력하세요", placeholder="예: 서울특별시 중구 세종대로 110")
facility_type = st.selectbox("🏢 원하는 공공시설을 선택하세요", ["도서관", "병원", "공원"])

# -------------------------------
# 지도 분석 실행
if address:
    # 주소를 위도/경도로 변환
    lat, lon = geocode_address(address)

    if lat and lon:
        # 위도, 경도 출력
        st.success(f"입력한 위치: 위도 {lat:.4f}, 경도 {lon:.4f}")

        # 지도를 생성 (초기 중심은 사용자 위치)
        m = folium.Map(location=[lat, lon], zoom_start=12)

        # 사용자 위치 마커 추가
        folium.Marker(
            [lat, lon],
            tooltip="🏠 사용자 위치",
            icon=folium.Icon(color='blue')
        ).add_to(m)

        # 선택한 시설 종류에 맞는 시설 리스트 가져오기
        facilities = get_facilities(facility_type)

        # 각 시설에 대해 거리, 점수 계산 및 마커 표시
        for f in facilities:
            facility_loc = (f["lat"], f["lon"])
            distance_km = geodesic((lat, lon), facility_loc).km  # 사용자와 시설 간 거리
            score = calculate_accessibility(distance_km)         # 접근성 점수 계산

            # 마커에 보여줄 정보
            popup = f"<b>{f['name']}</b><br>거리: {distance_km:.2f}km<br>접근성 지수: {score}"
            color = "green" if score > 70 else "orange" if score > 40 else "red"  # 점수에 따라 색상

            # 지도에 시설 마커 추가
            folium.Marker(
                location=facility_loc,
                popup=popup,
                tooltip=f"{f['name']} ({score})",
                icon=folium.Icon(color=color)
            ).add_to(m)

        # 지도 출력
        st.markdown("### 🗺️ 접근성 지도")
        st_folium(m, width=800, height=600)

    else:
        # 주소를 찾을 수 없을 경우
        st.error("❌ 주소를 찾을 수 없습니다. 다시 확인해주세요.")
