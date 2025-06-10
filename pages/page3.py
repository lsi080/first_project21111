import streamlit as st  # Streamlit 라이브러리 불러오기
import pandas as pd     # 데이터프레임 처리를 위한 pandas 불러오기
import datetime         # 날짜 입력을 위한 datetime 모듈 불러오기

# 앱 제목 및 설명 출력
st.title("💰 나만의 용돈 가계부")
st.write("수입과 지출을 입력하고, 나의 용돈을 관리해보세요!")

# 입력된 데이터를 저장할 리스트 초기화 (세션 상태에 저장)
# 페이지가 리로딩되어도 데이터를 유지하기 위해 session_state 사용
if "data" not in st.session_state:
    st.session_state["data"] = []

# 입력 폼 생성 (폼 이름은 "entry_form")
with st.form("entry_form"):
    # 날짜 입력 필드 (기본값은 오늘 날짜)
    date = st.date_input("📅 날짜", datetime.date.today())

    # 항목 선택 (카테고리 고정 리스트 제공)
    category = st.selectbox("📂 항목", ["용돈", "식비", "간식", "교통", "게임", "기타"])

    # 설명 입력란 (자유 텍스트)
    description = st.text_input("📝 설명", "")

    # 금액 입력란 (수입은 양수, 지출은 음수로 입력)
    amount = st.number_input("💸 금액 (수입은 +, 지출은 - 입력)", step=100)

    # 저장 버튼
    submitted = st.form_submit_button("저장하기")
    
    # 버튼 클릭 시 데이터 저장
    if submitted:
        st.session_state["data"].append({  # 입력된 데이터를 session_state에 추가
            "날짜": date,
            "항목": category,
            "설명": description,
            "금액": amount
        })
        st.success("저장되었습니다!")  # 저장 완료 메시지 출력

# 데이터가 존재할 경우 출력
if st.session_state["data"]:
    # 리스트를 DataFrame으로 변환
    df = pd.DataFrame(st.session_state["data"])

    # 입력된 내역 출력
    st.subheader("📊 입력된 내역")
    st.dataframe(df, use_container_width=True)  # 화면 너비에 맞춰 출력

    # 금액의 총합 계산 (현재 잔액)
    total = df["금액"].sum()
    st.metric("💼 현재 잔액", f"{total:,} 원")  # 천 단위 구분 쉼표 표시

    # 항목별 지출 차트 출력
    st.subheader("📈 항목별 지출 분석")

    # 금액이 0보다 작은 항목만 추출 (지출만 필터링)
    df_negative = df[df["금액"] < 0]

    if not df_negative.empty:
        # 항목별 지출 합계를 구하고 절댓값으로 변환
        category_sum = df_negative.groupby("항목")["금액"].sum().abs()

        # 막대 차트로 시각화
        st.bar_chart(category_sum)
    else:
        # 지출 데이터가 없는 경우 메시지 출력
        st.info("지출 내역이 아직 없습니다.")
else:
    # 데이터가 없을 때 초기 메시지 출력
    st.info("입력된 기록이 없습니다. 위의 폼을 이용해 기록을 추가해주세요.")
