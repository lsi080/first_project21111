import streamlit as st  # Streamlit 라이브러리 불러오기

# 기본 설정 (페이지 제목과 아이콘 설정)
st.set_page_config(page_title="체형 분석기", page_icon="💪")

# 앱 제목 출력
st.title("💪 남학생을 위한 체형 분석기")

# 앱 설명 출력
st.markdown("자신의 **신체 정보**를 입력하면 BMI와 기초대사량(BMR)을 계산해드립니다!")

# 사용자 입력 받기

# 키 입력 (cm 단위, 최소 100cm ~ 최대 250cm)
height = st.number_input("📏 키(cm)", min_value=100.0, max_value=250.0, step=0.1)

# 체중 입력 (kg 단위, 최소 30kg ~ 최대 200kg)
weight = st.number_input("⚖️ 체중(kg)", min_value=30.0, max_value=200.0, step=0.1)

# 나이 입력 (최소 10세 ~ 최대 100세)
age = st.number_input("🎂 나이", min_value=10, max_value=100, step=1)

# 골격근량 입력 (kg 단위, 최소 10kg ~ 최대 100kg)
muscle_mass = st.number_input("💪 골격근량(kg)", min_value=10.0, max_value=100.0, step=0.1)

# 체지방률 입력 (% 단위, 최소 1% ~ 최대 60%)
body_fat_pct = st.number_input("⚠️ 체지방률(%)", min_value=1.0, max_value=60.0, step=0.1)

# 버튼 클릭 시 결과 계산 및 출력
if st.button("📊 결과 확인"):

    # 키를 미터 단위로 변환
    height_m = height / 100

    # BMI 계산 (체중(kg) / (키(m) * 키(m)))
    bmi = weight / (height_m ** 2)
    
    # BMR(기초대사량) 계산 (Mifflin-St Jeor 공식, 남성 기준)
    # BMR = 10 * 체중 + 6.25 * 키 - 5 * 나이 + 5
    bmr = 10 * weight + 6.25 * height - 5 * age + 5

    # 결과 출력
    st.subheader("📈 분석 결과")

    # 계산된 BMI 출력
    st.write(f"**✅ BMI:** {bmi:.2f}")
    
    # BMI 수치에 따른 판정 메시지 출력
    if bmi < 18.5:
        st.warning("저체중입니다. 건강한 식습관과 운동이 필요해요.")
    elif bmi < 23:
        st.success("정상 체중입니다! 지금처럼 건강을 유지하세요.")
    elif bmi < 25:
        st.warning("과체중 경계입니다. 체지방률과 운동량을 체크해보세요.")
    else:
        st.error("비만입니다. 규칙적인 운동과 식단 조절이 중요합니다.")
    
    # BMR 출력
    st.write(f"**🔥 기초대사량(BMR):** {bmr:.2f} kcal/day")

    # 골격근량 출력
    st.write(f"**💪 골격근량:** {muscle_mass} kg")

    # 체지방률 출력
    st.write(f"**⚖️ 체지방률:** {body_fat_pct}%")

    # 기초대사량에 대한 추가 설명 제공
    st.info("💡 기초대사량은 하루에 아무것도 하지 않아도 소모되는 에너지 양이에요!")
