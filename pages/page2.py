import streamlit as st
import openai
import pandas as pd
import datetime
import time

openai.api_key = "YOUR_OPENAI_API_KEY"  # OpenAI API 키 설정

st.set_page_config(page_title="AI 맞춤형 공부 코치", layout="centered")
st.title("🤖 AI 기반 맞춤형 공부 코치 앱 (확장판)")

# --- 1. 사용자 성향 진단 ---
st.header("1️⃣ 사용자 성향 진단")
learning_style = st.selectbox(
    "학습 스타일을 선택하세요",
    ("읽고 쓰기", "듣고 말하기", "직접 해보기")
)
focus_style = st.selectbox(
    "집중하는 방식은 어떤 편인가요?",
    ("짧게 자주 집중", "한번에 오래 집중", "가끔 쉬면서 집중")
)

# --- 2. 공부 목표 설정 ---
st.header("2️⃣ 공부 목표 설정")
goal_subject = st.text_input("공부할 과목/주제 입력", "수학")
goal_hours = st.number_input("이번 주 목표 공부 시간 (시간)", min_value=1, max_value=100, value=10)

# --- 3. 공부 시간 자동 측정 타이머 ---
st.header("3️⃣ 공부 타이머")

if 'timer_running' not in st.session_state:
    st.session_state.timer_running = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'elapsed_seconds' not in st.session_state:
    st.session_state.elapsed_seconds = 0

def timer():
    if st.session_state.timer_running:
        st.session_state.elapsed_seconds = int(time.time() - st.session_state.start_time)

if st.session_state.timer_running:
    timer()

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⏯️ 시작" if not st.session_state.timer_running else "⏸️ 일시정지"):
        if not st.session_state.timer_running:
            st.session_state.start_time = time.time() - st.session_state.elapsed_seconds
            st.session_state.timer_running = True
        else:
            st.session_state.timer_running = False

with col2:
    if st.button("⏹️ 초기화"):
        st.session_state.timer_running = False
        st.session_state.elapsed_seconds = 0
        st.session_state.start_time = None

with col3:
    elapsed_time_str = str(datetime.timedelta(seconds=st.session_state.elapsed_seconds))
    st.write(f"공부 시간: {elapsed_time_str}")

# --- 4. 집중력 상태 입력 ---
st.header("4️⃣ 오늘 집중력 상태")
today_focus = st.slider("오늘 집중력은 어느 정도였나요? (1~10)", 1, 10, 5)

# --- 5. 공부 기록 저장 ---
st.header("5️⃣ 오늘 공부 기록 저장")

if st.button("✅ 오늘 공부 기록 저장하기"):
    # 공부 기록 데이터프레임 생성 or 불러오기
    today = datetime.date.today().strftime("%Y-%m-%d")
    elapsed_hours = round(st.session_state.elapsed_seconds / 3600, 2)
    new_data = {
        "날짜": today,
        "공부시간(시간)": elapsed_hours,
        "집중력": today_focus,
        "학습스타일": learning_style,
        "집중방식": focus_style,
        "목표과목": goal_subject
    }

    try:
        df = pd.read_csv("study_record.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=new_data.keys())

    df = df.append(new_data, ignore_index=True)
    df.to_csv("study_record.csv", index=False)
    st.success(f"✅ {today} 공부 기록 저장 완료! 공부시간: {elapsed_hours}시간")

# --- 6. 주간 공부 진행률 시각화 ---
st.header("6️⃣ 주간 공부 진행률")

try:
    df = pd.read_csv("study_record.csv")
    df['날짜'] = pd.to_datetime(df['날짜'])
    this_week = datetime.date.today() - datetime.timedelta(days=7)
    weekly_df = df[df['날짜'] >= pd.to_datetime(this_week)]

    if weekly_df.empty:
        st.info("이번 주 공부 기록이 없습니다.")
    else:
        # 날짜별 공부 시간 합산
        daily_sum = weekly_df.groupby(weekly_df['날짜'].dt.date)['공부시간(시간)'].sum()
        st.bar_chart(daily_sum)
        total = daily_sum.sum()
        st.write(f"이번 주 총 공부 시간: {total:.2f} 시간 / 목표: {goal_hours} 시간")
        st.progress(min(total / goal_hours, 1.0))
except FileNotFoundError:
    st.info("저장된 공부 기록이 없습니다.")

# --- 7. AI 맞춤형 공부 조언 ---
st.header("7️⃣ AI 맞춤형 공부 조언 받기")

if st.button("🤖 AI에게 공부 조언 받기"):
    prompt = f"""
    사용자의 학습 스타일은 '{learning_style}', 집중 방식은 '{focus_style}'입니다.
    오늘 공부 시간은 {round(st.session_state.elapsed_seconds / 3600, 2)}시간이고, 집중력은 {today_focus}/10입니다.
    공부 과목은 '{goal_subject}'이며, 이번 주 목표 공부 시간은 {goal_hours}시간입니다.
    이 정보를 바탕으로 공부 방법, 집중력 향상법, 목표 달성 팁 등을 친절하고 긍정적인 어조로 추천해주세요.
    """
    with st.spinner("AI가 공부 조언을 생성 중입니다..."):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )
    advice = response['choices'][0]['message']['content']
    st.markdown("### 📝 AI 맞춤 공부 조언")
    st.write(advice)

# --- 8. 집중력 향상 알림 (간단 팁 띄우기) ---
st.header("8️⃣ 집중력 향상 알림")

if today_focus <= 4:
    st.warning("⚠️ 오늘 집중력이 낮은 편이네요. 5분 스트레칭과 짧은 휴식을 권장합니다!")
elif today_focus >= 8:
    st.success("🎉 집중력이 매우 좋은 날입니다! 계속 이 페이스를 유지해봐요!")
else:
    st.info("👌 집중력이 보통인 날입니다. 적절한 휴식과 목표 설정이 중요합니다.")

