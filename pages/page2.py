# standby_power.py
import streamlit as st

def app():
    st.title("🔌 스마트 홈 – 대기 전력 차단 시뮬레이션")

    st.markdown("""
    일부 가전제품은 사용하지 않아도 대기 전력을 소비합니다. 자동 타이머를 설정해 대기 전력 절감을 시뮬레이션하세요.
    """)

    devices = {
        "TV": 5,  # W
        "전자레인지": 3,
        "게임기": 8,
        "오디오 시스템": 10,
        "셋탑박스": 6
    }

    st.write("각 기기의 **평균 대기 전력 소비**는 다음과 같습니다 (단위: W):")
    st.table(devices)

    hours_off = st.slider("하루에 타이머로 차단하는 시간 (시간)", 0, 24, 10)
    cost_per_kwh = 0.12

    total_saved_kwh = 0
    for device, watt in devices.items():
        saved_kwh = (watt * hours_off * 30) / 1000  # 한 달 기준
        total_saved_kwh += saved_kwh

    total_saved_cost = total_saved_kwh * cost_per_kwh

    st.subheader("한 달 기준 절감 효과")
    st.write(f"절약된 전력: **{total_saved_kwh:.2f} kWh**")
    st.write(f"절약된 비용: **${total_saved_cost:.2f}**")

    if total_saved_kwh > 5:
        st.success("타이머 설정으로 상당한 대기 전력을 절약할 수 있습니다!")
    else:
        st.info("절약량은 적지만, 작은 습관이 모이면 큰 절약으로 이어집니다.")
