import streamlit as st

def main():
    st.title("집 에너지 소비량 분석 및 절약 조언")

    st.write("하루 에너지 소비량(kWh)을 입력해주세요:")

    energy = st.number_input("에너지 소비량 (kWh)", min_value=0.0, step=0.1)

    # 기준 에너지 소비량 (예: 30 kWh 이상이면 많이 쓴 것)
    기준 = 30.0

    if energy == 0:
        st.info("에너지 소비량을 입력해 주세요.")
    else:
        if energy > 기준:
            st.warning(f"하루 {energy} kWh 사용, 기준({기준} kWh)보다 많이 사용했습니다.")
            st.subheader("에너지 절약을 위한 조언:")
            st.write("""
            - 불필요한 전자기기 전원 끄기
            - 고효율 LED 전구 사용하기
            - 가전제품 사용 시간을 줄이고, 대기 전력 차단하기
            - 에어컨, 난방 온도 적정 유지하기
            - 태양광 등 신재생 에너지 사용 고려하기
            """)
        else:
            st.success(f"하루 {energy} kWh 사용, 기준({기준} kWh)보다 적게 사용했습니다!")
            st.subheader("에너지 절약의 긍정적 영향:")
            st.write("""
            - 전기 요금 절감으로 경제적 이득
            - 온실가스 배출 감소로 환경 보호 기여
            - 에너지 자원 절약으로 지속 가능한 생활 가능
            - 지역사회 에너지 수요 감소로 전력 안정성 향상
            """)

if __name__ == "__main__":
    main()
