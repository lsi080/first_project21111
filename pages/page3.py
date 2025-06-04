import streamlit as st
import pandas as pd
import datetime

# 앱 제목
st.title("💰 나만의 용돈 가계부")
st.write("수입과 지출을 입력하고, 나의 용돈을 관리해보세요!")

# 입력 저장용 리스트 초기화
if "data" not in st.session_state:
    st.session_state["data"] = []

# 입력폼
with st.form("entry_form"):
    date = st.date_input("📅 날짜", datetime.date.today())
    category = st.selectbox("📂 항목", ["용돈", "식비", "간식", "교통", "게임", "기타"])
    description = st.text_input("📝 설명", "")
    amount = st.number_input("💸 금액 (수입은 +, 지출은 - 입력)", step=100)
    
    submitted = st.form_submit_button("저장하기")
    if submitted:
        st.session_state["data"].append({
            "날짜": date,
            "항목": category,
            "설명": description,
            "금액": amount
        })
        st.success("저장되었습니다!")

# 데이터프레임으로 변환
if st.session_state["data"]:
    df = pd.DataFrame(st.session_state["data"])
    st.subheader("📊 입력된 내역")
    st.dataframe(df, use_container_width=True)

    # 총합 계산
    total = df["금액"].sum()
    st.metric("💼 현재 잔액", f"{total:,} 원")

    # 항목별 지출 차트
    st.subheader("📈 항목별 지출 분석")
    df_negative = df[df["금액"] < 0]
    if not df_negative.empty:
        category_sum = df_negative.groupby("항목")["금액"].sum().abs()
        st.bar_chart(category_sum)
    else:
        st.info("지출 내역이 아직 없습니다.")
else:
    st.info("입력된 기록이 없습니다. 위의 폼을 이용해 기록을 추가해주세요.")
