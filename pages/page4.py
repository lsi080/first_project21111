import streamlit as st
import random

st.title("🎵 나만의 음악 추천기")
st.markdown("기분과 상황에 맞는 노래를 추천해드립니다. 오늘의 분위기에 어울리는 곡을 찾아보세요!")

# 사용자 입력
mood = st.selectbox("😊 현재 기분은?", ["기쁨", "슬픔", "화남", "편안함", "피곤함"])
time_of_day = st.selectbox("🕒 지금은 언제인가요?", ["아침", "점심", "저녁", "밤"])
genre = st.selectbox("🎧 듣고 싶은 장르는?", ["발라드", "팝", "힙합", "록", "로파이", "K-POP"])

# 방대한 음악 추천 데이터
music_db = {
    # 기쁨
    ("기쁨", "아침", "K-POP"): [
        ("NewJeans - Super Shy", "https://youtu.be/ArmDp-zijuc"),
        ("STAYC - ASAP", "https://youtu.be/INP0c7bh2r4"),
        ("Red Velvet - Power Up", "https://youtu.be/ESEoLxFd_4E")
    ],
    ("기쁨", "점심", "팝"): [
        ("Pharrell Williams - Happy", "https://youtu.be/ZbZSe6N_BXs"),
        ("Katy Perry - Firework", "https://youtu.be/QGJuMBdaqIw"),
        ("Dua Lipa - Levitating", "https://youtu.be/TUVcZfQe-Kw")
    ],
    ("기쁨", "저녁", "록"): [
        ("Imagine Dragons - On Top of the World", "https://youtu.be/w5tWYmIOWGk"),
        ("The Script - Hall of Fame", "https://youtu.be/mk48xRzuNvA")
    ],

    # 슬픔
    ("슬픔", "밤", "발라드"): [
        ("폴킴 - 너를 만나", "https://youtu.be/sWNpJlZgRQg"),
        ("김나영 - 솔직하게 말해서 나", "https://youtu.be/Snk-d-NnNxc"),
        ("이하이 - 한숨", "https://youtu.be/RhLbnWZk9nE")
    ],
    ("슬픔", "저녁", "K-POP"): [
        ("BTS - Spring Day", "https://youtu.be/xEeFrLSkMm8"),
        ("태연 - 그대라는 시", "https://youtu.be/4HG_CJzyX6A")
    ],

    # 화남
    ("화남", "점심", "힙합"): [
        ("Ash Island - Error", "https://youtu.be/2W0Sl4iN7Ks"),
        ("이영지 - Not Sorry", "https://youtu.be/hPVxQXJqbi4"),
        ("BewhY - Forever", "https://youtu.be/ulzkF6T_lgA")
    ],

    # 피곤함
    ("피곤함", "밤", "로파이"): [
        ("Lo-Fi Chill Mix", "https://youtu.be/jfKfPfyJRdk"),
        ("Late Night Vibes", "https://youtu.be/p60zRbCrn2E"),
        ("코딩할 때 듣기 좋은 로파이", "https://youtu.be/1hHMwLxN6EM")
    ],

    # 편안함
    ("편안함", "저녁", "발라드"): [
        ("성시경 - 거리에서", "https://youtu.be/82bpBPPm7k8"),
        ("임한별 - 이별하러 가는 길", "https://youtu.be/sCTj8D4WXJ8"),
        ("10cm - 폰서트", "https://youtu.be/qEJJLPOhNOo")
    ],

    # 기본값
    ("default", "default", "default"): [
        ("BTS - Dynamite", "https://youtu.be/gdZLi9oWNZg"),
        ("IU - Blueming", "https://youtu.be/D1PvIWdJ8xo")
    ]
}

# 추천 결과
key = (mood, time_of_day, genre)
recommendations = music_db.get(key, music_db.get(("default", "default", "default")))

song = random.choice(recommendations)

# 결과 출력
st.subheader("🎶 추천 노래")
st.write(f"**{song[0]}**")
st.video(song[1])
