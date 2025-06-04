import streamlit as st
import pandas as pd
import datetime
import random
import os

st.title("🧘 학생을 위한 멘탈 관리 & 감정 일기 앱")

# 명언 리스트 (더 추가 가능)
quotes = [
    "어려움은 성장의 기회입니다.",
    "오늘의 노력은 내일의 힘이 됩니다.",
    "작은 변화가 큰 변화를 만듭니다.",
    "실패는 성공의 어머니입니다.",
    "지금 이 순간을 소중히 여기세요."
]

# 스트레스 관리 팁 리스트
tips = [
    "5분간 깊게 숨쉬기 연습을 해보세요.",
    "가벼운 스트레칭이나 산책으로 몸을 움직이세요.",
    "좋아하는 음악을 듣고 잠시 휴식을 취하세요.",
    "긍정적인 자기 대화를 시도해보세요.",
    "일정을 분리하여 작은 목표부터 하나씩 달성해보세요."
]

# 오늘 날짜
today = datetime.date.today().strftime("%Y-%m-%d")

# 감정 상태 입력
st.header("1️⃣ 오늘의 감정을 기록해 주세요")
emotion = st.selectbox(
    "오늘 당신의 기분은 어떤가요?",
    ["매우 좋음 😊", "좋음 🙂", "보통 😐", "나쁨 😟", "매우 나쁨 😢"]
)

# 오늘 느낀 점 간단히 작성
st.header("2️⃣ 오늘의 감정이나 생각을 간단히 적어주세요")
diary = st.text_area("여기에 작성하세요...", max_chars=300)

# 저장 버튼
if st.button("기록 저장하기"):
    new_record = {
        "날짜": today,
        "감정": emotion,
        "일기": diary
    }

    filename = "mental_diary.csv"

    if os.path.exists(filename):
        df = pd.read_csv(filename)
        # 날짜 중복 방지 위해 오늘 기록이 있으면 덮어쓰기
        df = df[df['날짜'] != today]
        df = df.append(new_record, ignore_index=True)
    else:
        df = pd.DataFrame([new_record])

    df.to_csv(filename, index=False)
    st.success("오늘의 감정 기록이 저장되었습니다!")

# 오늘의 긍정 명언 & 스트레스 관리 팁
st.header("3️⃣ 오늘의 긍정 명언과 스트레스 관리 팁")
st.markdown(f"> {random.choice(quotes)}")
st.info(random.choice(tips))

# 감정 일기 확인
st.header("4️⃣ 지난 감정 기록 보기")
if os.path.exists("mental_diary.csv"):
    df = pd.read_csv("mental_diary.csv")
    df = df.sort_values(by="날짜", ascending=False)
    for i, row in df.iterrows():
        st.write(f"**{row['날짜']}** - 감정: {row['감정']}")
        if row['일기']:
            st.write(f"> {row['일기']}")
        st.write("---")
else:
    st.write("아직 기록된 감정 일기가 없습니다.")
