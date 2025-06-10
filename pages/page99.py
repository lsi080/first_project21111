# solar_energy.py
import streamlit as st

def app():
    st.title("🔆 스마트 홈 – 태양광 발전량 예측")

    st.markdown("""
    설치된 태양광 패널의 발전량을 계산하고, 에너지 소비 대비 자가 발전 비율을 확인할 수 있습니다.
    """)

    panel_area = st.number_input("태양광 패널 설치 면적 (㎡)", min_value=0.0, step=0.5)
    efficiency = st.slider("패널 효율 (%)", min_value=10, max_value=25, value=18)
    sunlight_hours = st.slider("일일 평균 일조 시간 (시간)", 0.0, 12.0, 4.5, 0.5)
    household_consumption = st.number_input("가정의 하루 전력 소비량 (kWh)", min_value=0.0, value=10.0)

    if panel_area > 0 and sunlight_hours > 0:
        generation_kwh = panel_area * (efficiency / 100) * sunlight_hours
        self_supply_ratio = (generation_kwh / household_consumption) * 100 if household_consumption else 0

        st.subheader("예상 태양광 발전량")
        st.write(f"일일 발전량: **{generation_kwh:.2f} kWh**")
        st.write(f"자가 발전 비율: **{self_supply_ratio:.1f}%**")

        if self_supply_ratio >= 80:
            st.success("대부분의 전기를 자가 발전으로 충당할 수 있습니다!")
        elif self_supply_ratio >= 40:
            st.info("전기의 일부를 자가 발전으로 커버하고 있습니다.")
        else:
            st.warning("자가 발전량이 부족합니다. 에너지 절약을 병행하세요.")
