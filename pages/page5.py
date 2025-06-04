import streamlit as st
import requests
import random

# OpenWeather API 키 입력 (여기에 본인의 키 입력)
API_KEY = "여기에_당신의_API_키를_입력하세요"  # 예: abc123def456ghi789

st.title("🌤️ 날씨에 어울리는 영상 추천기 (한글 지역 지원)")
st.markdown("**대한민국 전 지역 이름**을 한글로 입력하세요! (예: 서울, 대구, 전주, 제주 등)")

# 한글 도시명 입력
city_kr = st.text_input("📍 지역 이름을 입력하세요", "서울")

# 날씨 요청 처리
if st.button("🔍 날씨 확인 & 영상 추천"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_kr},KR&appid={API_KEY}&lang=kr&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["main"]  # 예: Clear, Rain, Snow, Clouds 등
        temp = data["main"]["temp"]

        st.success(f"현재 **{city_kr}**의 날씨는 **{weather}**, 온도는 {temp}°C 입니다.")

        # 날씨별 추천 영상 데이터베이스
        video_db = {
            "Clear": [
                ("☀️ 맑은 날 상쾌한 음악", "https://youtu.be/8ybW48rKBME"),
                ("산책하면서 듣기 좋은 K-POP", "https://youtu.be/ArmDp-zijuc")
            ],
            "Rain": [
                ("🌧️ 빗소리 로파이", "https://youtu.be/e3L1PIY1pN8"),
                ("비 오는 날 감성 발라드", "https://youtu.be/sWNpJlZgRQg")
            ],
            "Clouds": [
                ("⛅ 흐린 날 재즈", "https://youtu.be/1ZYbU82GVz4"),
                ("잔잔한 음악과 함께", "https://youtu.be/DWcJFNfaw9c")
            ],
            "Snow": [
                ("❄️ 눈 오는 날 ASMR", "https://youtu.be/VF-r5TtlT9w"),
                ("겨울 감성 음악", "https://youtu.be/-cCwbU-JR6Y")
            ],
            "Thunderstorm": [
                ("⚡ 격한 힙합 비트", "https://youtu.be/nOB7UZz72g8"),
                ("천둥 속 집중 음악", "https://youtu.be/TL7QZ6uwcUQ")
            ],
            "Drizzle": [
                ("🌦️ 이슬비처럼 잔잔한 재즈", "https://youtu.be/vBGiFtb8Rpw")
            ]
        }

        # 기본 영상
        recommended = video_db.get(weather, [
            ("☁️ 일반 날씨용 기본 음악", "https://youtu.be/gdZLi9oWNZg")
        ])

        # 무작위 추천
        title, link = random.choice(recommended)
        st.subheader("🎬 추천 영상")
        st.write(f"**{title}**")
        st.video(link)

    else:
        st.error("😥 날씨 정보를 불러올 수 없습니다. 지역명을 정확히 입력했는지 확인해보세요. (예: 전주, 여수, 강릉 등)")
