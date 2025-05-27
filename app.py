import streamlit as st

st.title("🧠 사용자 성향 파악 설문")

st.write("아래 질문에 답해주세요. 당신의 공부 성향을 분석해 드립니다.")

# 1. 학습 스타일
learning_style = st.radio(
    "당신은 어떤 학습 스타일인가요?",
    ("읽고 쓰는 걸 좋아함", "듣고 말하는 걸 좋아함", "직접 행동하며 배우는 걸 좋아함")
)

# 2. 집중 지속 시간
focus_duration = st.selectbox(
    "한 번에 얼마나 오래 집중할 수 있나요?",
    ("10분 이내", "10~30분", "30분 이상")
)

# 3. 공부 환경 선호도
study_env = st.multiselect(
    "어떤 공부 환경을 선호하나요? (복수 선택 가능)",
    ["조용한 곳", "배경음악 있음", "사람 많은 곳", "카페 같은 곳", "자유로운 분위기"]
)

# 4. 목표 설정 방식
goal_setting = st.radio(
    "목표 설정은 어떤 방식을 선호하나요?",
    ("작고 구체적인 목표 세우기", "크고 포괄적인 목표 세우기", "그때그때 느낌에 따라 공부")
)

if st.button("성향 분석 결과 보기"):
    st.header("🎯 당신의 공부 성향 분석")

    # 간단한 성향 분석 및 피드백
    feedback = ""

    if learning_style == "읽고 쓰는 걸 좋아함":
        feedback += "- 당신은 시각적 학습자입니다. 노트 필기나 플래시카드를 활용하면 효과적입니다.\n"
    elif learning_style == "듣고 말하는 걸 좋아함":
        feedback += "- 당신은 청각적 학습자입니다. 강의 듣기나 소리 내어 읽기가 도움이 됩니다.\n"
    else:
        feedback += "- 당신은 체험적 학습자입니다. 직접 실습하거나 문제를 풀면서 배우는 걸 추천합니다.\n"

    if focus_duration == "10분 이내":
        feedback += "- 집중 시간이 짧은 편이니, 짧은 공부 세션과 자주 쉬는 것이 좋습니다.\n"
    elif focus_duration == "10~30분":
        feedback += "- 중간 정도 집중력을 가지고 있어, 25분 공부 후 5분 휴식 같은 포모도로 기법이 효과적일 수 있습니다.\n"
    else:
        feedback += "- 오랜 시간 집중 가능하니, 몰입하여 깊게 공부하는 걸 추천합니다.\n"

    if "조용한 곳" in study_env:
        feedback += "- 조용한 환경이 집중에 도움이 됩니다.\n"
    if "배경음악 있음" in study_env:
        feedback += "- 적절한 배경음악은 집중력을 높여줍니다.\n"
    if "사람 많은 곳" in study_env or "카페 같은 곳" in study_env:
        feedback += "- 주변 소음이 어느 정도 있어야 집중이 잘 되는 타입입니다.\n"

    if goal_setting == "작고 구체적인 목표 세우기":
        feedback += "- 세분화된 목표를 세우고 하나씩 달성하는 방식이 효과적입니다.\n"
    elif goal_setting == "크고 포괄적인 목표 세우기":
        feedback += "- 큰 그림을 먼저 그리고 그에 맞춰 계획을 세우는 편입니다.\n"
    else:
        feedback += "- 유동적으로 공부 계획을 세우며 융통성 있게 공부합니다.\n"

    st.markdown(feedback)
