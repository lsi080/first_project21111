import streamlit as st

# 에너지 소비 계산 함수
def calculate_energy_consumption(power, hours, cost_per_kwh):
    """전력 소비 계산 함수 (단위: kWh)"""
    consumption = (power * hours) / 1000  # kWh 단위로 변환
    cost = consumption * cost_per_kwh  # 비용 계산
    return consumption, cost

# 에너지 절약 팁 제공 함수
def energy_saving_tips(consumption):
    """에너지 절약 팁 제공 함수"""
    if consumption < 5:
        return "에너지 소비가 낮습니다! 계속 이렇게 유지하세요!"
    elif consumption < 10:
        return "에너지 소비를 조금 더 줄일 수 있어요. 전기 제품을 사용하지 않을 때 끄는 습관을 들여보세요."
    else:
        return "에너지 소비가 많이 높아요! 가전 제품 사용을 줄이고 효율적인 제품으로 교체하세요!"

# Streamlit 앱
def app():
    st.title("스마트 홈 에너지 관리 시스템")
    st.markdown("""
    이 시스템은 집안의 전력 소비를 분석하여, 에너지 절약 방법을 제시합니다. 
    집안의 각 기기들의 전력 소비를 입력하고, 총 소비량을 확인하세요.
    """)

    # 전력 소비를 입력할 기기 리스트
    devices = ['조명', '에어컨', '냉장고', '세탁기', '컴퓨터']
    device_data = []

    # 각 기기의 전력 소비량 입력 받기
    for device in devices:
        power = st.number_input(f"{device}의 전력 소비 (W)", min_value=0, step=10, key=device)
        hours = st.number_input(f"{device}의 사용 시간 (시간)", min_value=0, step=1, key=f"{device}_time")
        device_data.append({'device': device, 'power': power, 'hours': hours})

    # 각 기기의 에너지 소비 계산
    total_consumption = 0
    total_cost = 0
    energy_data = []
    cost_per_kwh = 0.12  # 1kWh당 비용 (예시: 0.12달러/kWh)

    for data in device_data:
        consumption, cost = calculate_energy_consumption(data['power'], data['hours'], cost_per_kwh)
        energy_data.append({'device': data['device'], 'consumption': consumption, 'cost': cost})
        total_consumption += consumption
        total_cost += cost

    # 결과 출력
    st.subheader("기기별 에너지 소비 및 비용")
    for data in energy_data:
        st.write(f"{data['device']} : {data['consumption']:.2f} kWh 소비, 비용: ${data['cost']:.2f}")

    st.subheader("총 에너지 소비 및 비용")
    st.write(f"총 소비 전력: {total_consumption:.2f} kWh")
    st.write(f"총 비용: ${total_cost:.2f}")

    # 에너지 절약 팁 제공
    saving_tip = energy_saving_tips(total_consumption)
    st.subheader("에너지 절약 팁")
    st.write(saving_tip)

# Streamlit 앱 실행
if __name__ == "__main__":
    app()
