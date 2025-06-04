import streamlit as st
import requests
import random

# 👉 자신의 OpenWeather API 키 입력
API_KEY = "여기에_당신의_API_키를_입력하세요"  # 예: abc123def456ghi789

st.title("🌦️ 날씨에 어울리는 영상 추천기")
st.markdown("현재 날씨에 맞춰 기분 좋은 영상을 추천해드립니다!")

# 도시 입력
city = st.text_input("🏙️ 도시 이름을 입력하세요 (예: Seoul, Busan)", "Seoul")

# 날씨 요청
if st.button("🔍 날씨 확인 & 영상 추천"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=kr&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["main"]  # 예: Clear, Rain, Snow, Clouds 등
        temp = data["main"]["temp"]

        st.success(f"현재 {city}의 날씨는 **{weather}**, 온도는 {temp}°C입니다.")

        # 날씨별 추천 영상 DB
        video_db = {
            "Clear": [
                ("☀️ 맑은 날 듣기 좋은 상쾌한 음악", "https://youtu.be/8ybW48rKBME"),
                ("산책하면서 듣기 좋은 K-POP", "https://youtu.be/ArmDp-zijuc")
            ],
            "Rain": [
                ("🌧️ 빗소리와 함께하는 로파이", "https://youtu.be/e3L1PIY1pN8"),
                ("비 오는 날 감성 발라드", "https://youtu.be/sWNpJlZgRQg")
            ],
            "Clouds": [
                ("⛅ 흐린 날 어울리는 잔잔한 음악", "https://youtu.be/1ZYbU82GVz4"),
                ("카페에서 듣는 듯한 음악", "https://youtu.be/DWcJFNfaw9c")
            ],
            "Snow": [
                ("❄️ 눈 오는 날 ASMR", "https://youtu.be/VF-r5TtlT9w"),
                ("겨울 감성 음악", "https://youtu.be/-cCwbU-JR6Y")
            ],
            "Thunderstorm": [
                ("⚡ 천둥치는 날 어울리는 집중 음악", "https://youtu.be/TL7QZ6uwcUQ"),
                ("격한 감정의 힙합 비트", "https://youtu.be/nOB7UZz72g8")
            ],
            "Drizzle": [
                ("🌦️ 이슬비처럼 잔잔한 재즈", "https://youtu.be/vBGiFtb8Rpw")
            ]
        }

        # 기본값 처리
        recommended = video_db.get(weather, [
            ("기본 영상", "https://youtu.be/gdZLi9oWNZg")
        ])

        # 무작위 추천
        title, link = random.choice(recommended)
        st.subheader("🎬 추천 영상")
        st.write(f"**{title}**")
        st.video(link)

    else:
        st.error("도시 이름을 확인해주세요. (예: Seoul, Tokyo, London)")
