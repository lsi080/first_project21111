import streamlit as st  # Streamlit 라이브러리 임포트
import math  # 수학 관련 함수 사용을 위한 임포트

# 사용자로부터 하루 전력 사용량(kWh)을 입력받음
usage = st.number_input("하루 전력 사용량을 입력하세요 (kWh)", min_value=0.0, step=0.1, format="%.1f")

# 입력값이 0보다 클 때만 계산 실행
if usage > 0:
    co2_per_kwh = 0.424  # kWh 당 배출되는 이산화탄소(kg), 한국 전력 통계 기준
    tree_absorption_daily = 6.6 / 365  # 나무 한 그루가 하루에 흡수하는 CO2 (kg, 연간 6.6kg 기준)

    co2_emission = usage * co2_per_kwh  # 사용 전력에 따른 총 이산화탄소 배출량 계산 (kg)
    equivalent_trees = co2_emission / tree_absorption_daily  # 이산화탄소를 흡수하기 위해 필요한 나무 수 계산
    tree_count = math.ceil(equivalent_trees)  # 나무 수를 올림 처리하여 정수로 변환

    # 결과를 성공 메시지로 출력 (나무 수 표시)
    st.success(f"🌳 하루 전력 사용량은 약 **{equivalent_trees:.1f}그루의 나무**가 흡수해야 하는 탄소량입니다.")

    max_display = min(tree_count, 100)  # 최대 100그루까지만 이모지로 표시하도록 제한
    st.markdown("".join(["🌳"] * max_display))  # 나무 이모지를 tree_count 만큼 반복 출력

    # 나무 수가 100그루를 초과하면 안내 메시지 출력
    if tree_count > 100:
        st.info(f"※ 너무 많은 나무라 최대 100그루까지만 표시했습니다. 실제 필요 나무 수: {tree_count}그루")

    # 전력 절약을 위한 팁을 마크다운 형식으로 출력
    st.markdown("### 🔌 전력 절약 팁")
    st.markdown("""
    - 💡 LED 조명 사용하기  
    - 🔌 사용하지 않는 전자제품 플러그 뽑기  
    - 🌡️ 에어컨 온도 1도 올리기  
    - 🚿 절수 샤워기 사용하기  
    - 🕒 대기전력 차단 멀티탭 사용하기  
    """)
