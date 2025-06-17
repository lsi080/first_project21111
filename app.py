import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="우리집 번개맨", page_icon="⚡", layout="centered")

# 스타일을 위한 CSS
st.markdown(
    """
    <style>
    .title-text {
        text-align: center;
        font-size: 60px;
        font-weight: bold;
        background: linear-gradient(to right, #007BFF, #FFD700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 100px;
    }
    .subtitle-text {
        text-align: center;
        font-size: 24px;
        margin-top: 20px;
        color: #444444;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 제목 표시
st.markdown('<div class="title-text">우리집 번개맨</div>', unsafe_allow_html=True)

# 환영 메시지
st.markdown('<div class="subtitle-text">이곳에 오신 걸 환영합니다!</div>', unsafe_allow_html=True)
