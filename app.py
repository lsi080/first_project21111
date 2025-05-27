import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
import io

st.title("📚 시험 공부 계획 자동 생성기")

# 1. 시험 날짜 입력
exam_date = st.date_input("시험 날짜를 선택하세요", min_value=datetime.today().date() + timedelta(days=1))

# 2. 쉬는 요일 선택
rest_days = st.multiselect(
    "쉬는 요일을 선택하세요 (예: 토요일, 일요일은 공부 안 함)",
    options=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    default=["Saturday", "Sunday"]
)

# 3. 공부할 항목 입력
tasks_input = st.text_area("공부할 내용을 줄마다 입력하세요 (예: 챕터 1, 챕터 2, ...)", height=200)

# 4. 버튼 클릭 시 계획 생성
if st.button("공부 계획 생성하기"):
    tasks = [task.strip() for task in tasks_input.strip().split("\n") if task.strip()]

    if not tasks:
        st.warning("공부할 내용을 최소 1개 이상 입력해 주세요.")
    else:
        today = datetime.today().date()
        days_range = pd.date_range(start=today, end=exam_date - timedelta(days=1))
        
        # 쉬는 날 제외한 날짜 목록
        study_days = [day.date() for day in days_range if day.strftime("%A") not in rest_days]

        if len(study_days) == 0:
            st.warning("쉬는 날을 제외하면 공부할 수 있는 날이 없습니다.")
        else:
            # 공부 항목을 날짜에 균등하게 배분
            plan = []
            for i, task in enumerate(tasks):
                study_date = study_days[i % len(study_days)]
                plan.append((study_date, study_date.strftime('%A'), task))

            # DataFrame 생성 및 정렬
            plan_df = pd.DataFrame(plan, columns=["날짜", "요일", "공부할 내용"]).sort_values("날짜")

            st.success("📆 아래는 자동 생성된 공부 계획입니다:")
            st.dataframe(plan_df, use_container_width=True)

            # CSV 다운로드 버튼
            csv_buffer = io.StringIO()
            plan_df.to_csv(csv_buffer, index=False, encoding='utf-8-sig')
            st.download_button(
                label="📥 계획 다운로드 (CSV)",
                data=csv_buffer.getvalue(),
                file_name="study_plan.csv",
                mime="text/csv"
            )
