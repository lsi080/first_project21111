import streamlit as st

# 에너지 소비 계산 함수
def calculate_energy_consumption(power, hours, cost_per_kwh):
    """전력 소비 계산 함수 (단위: kWh)"""
    consumption = (power * hours) / 1000  # 전력 소비량 계산 (W * 시간 / 1000 = kWh)
    cost = consumption * cost_per_kwh  # 소비량에 따라 비용 계산 (kWh * 비용)
    return consumption, cost

# 에너지 절약 팁 제공 함수
def energy_saving_tips(consumption):
    """에너지 소비에 따른 절약 팁을 제공하는 함수"""
    if consumption < 5:
        return "에너지 소비가 낮습니다! 계속 이렇게 유지하세요!"  # 소비량이 적을 경우
    elif consumption < 10:
        return "에너지 소비를 조금 더 줄일 수 있어요. 전기 제품을 사용하지 않을 때 끄는 습관을 들여보세요."  # 소비량이 중간일 경우
    else:
        return "에너지 소비가 많이 높아요! 가전 제품 사용을 줄이고 효율적인 제품으로 교체하세요!"  # 소비량이 높을 경우

# Streamlit 앱
def app():
    st.title("스마트 홈 에너지 관리 시스템")  # 앱 제목
    st.markdown("""
    이 시스템은 집안의 전력 소비를 분석하여, 에너지 절약 방법을 제시합니다. 
    집안의 각 기기들의 전력 소비를 입력하고, 총 소비량을 확인하세요.
    """)

    # 전력 소비를 입력할 기기 리스트
    devices = ['조명', '에어컨', '냉장고', '세탁기', '컴퓨터']  # 기기 목록
    device_data = []  # 기기별 소비 데이터를 저장할 리스트

    # 각 기기의 전력 소비량과 사용 시간을 입력 받기
    for device in devices:
        power = st.number_input(f"{device}의 전력 소비 (W)", min_value=0, step=10, key=device)  # 전력 소비량 입력 (W)
        hours = st.number_input(f"{device}의 사용 시간 (시간)", min_value=0, step=1, key=f"{device}_time")  # 사용 시간 입력 (시간)
        device_data.append({'device': device, 'power': power, 'hours': hours})  # 입력된 값 저장

    # 각 기기의 에너지 소비 계산
    total_consumption = 0  # 총 소비량 초기화
    total_cost = 0  # 총 비용 초기화
    energy_data = []  # 각 기기별 에너지 소비 데이터를 저장할 리스트
    cost_per_kwh = 0.12  # 1kWh당 비용 (예시: 0.12달러/kWh)

    # 각 기기별로 에너지 소비량과 비용을 계산
    for data in device_data:
        consumption, cost = calculate_energy_consumption(data['power'], data['hours'], cost_per_kwh)  # 소비량과 비용 계산
        energy_data.append({'device': data['device'], 'consumption': consumption, 'cost': cost})  # 계산된 데이터 저장
        total_consumption += consumption  # 총 소비량에 추가
        total_cost += cost  # 총 비용에 추가

    # 결과 출력
    st.subheader("기기별 에너지 소비 및 비용")  # 기기별 소비 및 비용 제목
    for data in energy_data:
        # 각 기기별 소비량과 비용을 출력
        st.write(f"{data['device']} : {data['consumption']:.2f} kWh 소비, 비용: ${data['cost']:.2f}")

    st.subheader("총 에너지 소비 및 비용")  # 총 소비 및 비용 제목
    st.write(f"총 소비 전력: {total_consumption:.2f} kWh")  # 총 소비량 출력
    st.write(f"총 비용: ${total_cost:.2f}")  # 총 비용 출력

    # 에너지 절약 팁 제공
    saving_tip = energy_saving_tips(total_consumption)  # 총 소비량에 맞는 절약 팁 가져오기
    st.subheader("에너지 절약 팁")  # 절약 팁 제목
    st.write(saving_tip)  # 절약 팁 출력

# Streamlit 앱 실행
if __name__ == "__main__":
    app()  # 앱 실행
