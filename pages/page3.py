import streamlit as st
import matplotlib.pyplot as plt
import math

# 계산 기준 상수
CO2_PER_KWH = 0.423  # kg CO2 per kWh (대한민국 평균, 2023 기준 대략치)
CO2_ABSORBED_PER_TREE = 6.6  # kg CO2 per tree per year (연간 1그루 나무가 흡수하는 이산화탄소량)

st.set_page_config(page_title="에너지 소비와 나무", layout="centered")

# 타이틀
st.title("🌳 당신의 에너지 소비는 나무 몇 그루와 맞먹을까?")
st.write("당신이 사용하는 전기의 이산화탄소 배출량을 계산하고, 이를 상쇄하려면 **몇 그루의 나무**가 필요한지 알아보세요.")

# 사용자 입력
energy_kwh = st.number_input("💡 연간 전기 소비량 (kWh)", min_value=0.0, step=0.1, value=3500.0)

# 계산
co2_emission = energy_kwh * CO2_PER_KWH
tree_count = math.ceil(co2_emission / CO2_ABSORBED_PER_TREE)

# 결과 출력
st.subheader("📊 결과")

col1, col2 = st.columns(2)

with col1:
    st.metric("CO₂ 배출량", f"{co2_emission:,.2f} kg")

with col2:
    st.metric("필요한 나무 수", f"{tree_count} 그루")

# 시각화 - 나무 그림 이모지
st.subheader("🌲 나무로 시각화")
tree_emoji = "🌲"
max_display = 100

if tree_count <= max_display:
    trees = tree_emoji * tree_count
    st.markdown(f"<div style='font-size: 24px;'>{trees}</div>", unsafe_allow_html=True)
else:
    st.write(f"나무가 너무 많아 이모지로 모두 표시할 수는 없어요! 😅")
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(["필요한 나무"], [tree_count], color="green")
    ax.set_ylabel("나무 수")
    ax.set_title("필요한 나무 수")
    st.pyplot(fig)

# 정보
st.info("1kWh당 약 0.423kg의 CO₂가 배출되며, 1그루의 나무는 연간 약 6.6kg의 CO₂를 흡수한다고 가정합니다.")
