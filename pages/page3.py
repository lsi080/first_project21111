import streamlit as st
import math

usage = st.number_input("하루 전력 사용량을 입력하세요 (kWh)", min_value=0.0, step=0.1, format="%.1f")

if usage > 0:
    co2_per_kwh = 0.424  # kg CO2 per kWh (한국 기준)
    tree_absorption_daily = 6.6 / 365  # kg CO2 per tree per day

    co2_emission = usage * co2_per_kwh
    equivalent_trees = co2_emission / tree_absorption_daily
    tree_count = math.ceil(equivalent_trees)

    st.success(f"🌳 하루 전력 사용량은 약 **{equivalent_trees:.1f}그루의 나무**가 흡수해야 하는 탄소량입니다.")

    max_display = min(tree_count, 100)
    st.markdown("".join(["🌳"] * max_display))

    if tree_count > 100:
        st.info(f"※ 너무 많은 나무라 최대 100그루까지만 표시했습니다. 실제 필요 나무 수: {tree_count}그루")

    st.markdown("### 🔌 전력 절약 팁")
    st.markdown("""
    - 💡 LED 조명 사용하기  
    - 🔌 사용하지 않는 전자제품 플러그 뽑기  
    - 🌡️ 에어컨 온도 1도 올리기  
    - 🚿 절수 샤워기 사용하기  
    - 🕒 대기전력 차단 멀티탭 사용하기  
    """)
