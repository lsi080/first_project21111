import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="환영합니다!",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="auto"
)

# 이쁘게 보이는 제목과 서브 텍스트
st.markdown(
    """
    <div style="text-align: center; padding: 2rem;">
        <h1 style="color: #ff69b4;">🌸 이 곳에 오신 것을 진심으로 환영합니다! 🌸</h1>
        <p style="font-size: 1.2rem;">여기는 여러분을 위한 특별한 공간입니다.</p>
        <hr style="border: 1px solid #f0c0cb; width: 60%;">
    </div>
    """,
    unsafe_allow_html=True
)

# 간단한 애니메이션 느낌 (텍스트 효과)
st.success("즐거운 경험이 되시길 바랍니다!")

# 본문이 시작될 수 있는 자리
st.write("여기서부터 본격적인 앱 기능이 시작됩니다.")
