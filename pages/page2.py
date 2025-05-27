import streamlit as st
from datetime import datetime, timedelta

st.title("📅 시험 대비 공부 계획 생성기")

# 시험 날짜 입력
exam_date = st.date_input("시험 날짜를 선택하세요", min_value=datetime.today().date())

# 과목별 남은 진도 입력
st.header("과목별 남은 진도 입력")
subjects = st.text_area("시험 과목명을 콤마(,)로 구분해 입력하세요", "수학,영어,과학")
subject_list = [s.strip() for s in subjects.split(",") if s.strip()]

remaining_progress = {}
for subj in subject_list:
    remaining = st.number_input(f"{subj} 남은 진도(단원 수 또는 챕터 수)", min_value=0, value=5, step=1)
    remaining_progress[subj] = remaining

# 하루 공부 가능한 시간
study_hours_per_day = st.number_input("하루에 공부할 수 있는 시간(시간)", min_value=1, max_value=24, value=4)

# 시작 버튼
if st.button("📋 공부 계획 생성"):
    today = datetime.today().date()
    days_left = (exam_date - today).days + 1  # 오늘 포함
    if days_left <= 0:
        st.error("시험 날짜가 오늘이거나 지났습니다. 올바른 날짜를 선택하세요.")
    elif not subject_list:
        st.error("과목을 하나 이상 입력하세요.")
    else:
        # 총 남은 진도 합
        total_units = sum(remaining_progress.values())
        if total_units == 0:
            st.warning("남은 진도가 0입니다. 계획이 필요하지 않을 수 있습니다.")
        else:
            st.success(f"시험까지 {days_left}일 남았습니다.")
            st.write(f"총 남은 진도: {total_units} 단원(챕터)")

            # 하루에 처리할 단원 수 계산 (단순 균등 분배)
            units_per_day = total_units / days_left

            # 요일별 계획 생성
            plan = {}
            current_date = today
            remain_units = remaining_progress.copy()

            for i in range(days_left):
                day_plan = {}
                for subj in remain_units:
                    if remain_units[subj] <= 0:
                        day_plan[subj] = 0
                    else:
                        # 비율대로 나눠줌
                        day_share = (remaining_progress[subj] / total_units) * units_per_day
                        # 최대 남은 진도보다 크지 않게 조절
                        day_share = min(day_share, remain_units[subj])
                        day_plan[subj] = round(day_share, 2)
                        remain_units[subj] -= day_share
                plan[current_date.strftime("%Y-%m-%d (%a)")] = day_plan
                current_date += timedelta(days=1)

            # 계획 출력
            st.header("📅 요일별 공부 계획")
            for day, subjects_plan in plan.items():
                st.subheader(day)
                for subj, units in subjects_plan.items():
                    if units > 0:
                        st.write(f"- {subj}: {units} 단원 공부하기")
                st.write("---")
