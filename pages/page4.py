import streamlit as st
import random

st.title("🎨 취향 저격 배경화면 추천기")

# 1. 스타일 선택
style = st.selectbox(
    "좋아하는 배경화면 스타일을 선택하세요",
    ["자연", "도시", "미니멀", "추상", "우주", "동물", "기타"]
)

# 2. 색상 톤 선택
color_tone = st.radio(
    "선호하는 색상 톤은?",
    ["밝음", "어둠", "컬러풀", "모노크롬"]
)

# 3. 이미지 데이터베이스 (예시)
image_db = {
    "자연": {
        "밝음": [
            "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=60",
            "https://images.unsplash.com/photo-1469474968028-56623f02e42e?auto=format&fit=crop&w=800&q=60"
        ],
        "어둠": [
            "https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=800&q=60"
        ],
        "컬러풀": [
            "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?auto=format&fit=crop&w=800&q=60"
        ],
        "모노크롬": [
            "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=60"
        ]
    },
    "도시": {
        "밝음": [
            "https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=800&q=60"
        ],
        "어둠": [
            "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?auto=format&fit=crop&w=800&q=60"
        ],
        "컬러풀": [
            "https://images.unsplash.com/photo-1520975922981-0aa9333c48e6?auto=format&fit=crop&w=800&q=60"
        ],
        "모노크롬": [
            "https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=800&q=60"
        ]
    },
    # ... 다른 스타일도 유사하게 추가 가능
}

if st.button("추천 받기"):
    if style in image_db and color_tone in image_db[style]:
        imgs = image_db[style][color_tone]
        chosen_img = random.choice(imgs)
        st.image(chosen_img, caption=f"{style} 스타일 / {color_tone} 톤", use_column_width=True)

        if st.button("이미지 다운로드"):
            import urllib.request
            from io import BytesIO
            import base64

            with urllib.request.urlopen(chosen_img) as response:
                img_bytes = response.read()

            b64 = base64.b64encode(img_bytes).decode()
            href = f'<a href="data:file/jpg;base64,{b64}" download="background.jpg">⬇️ 이미지 다운로드</a>'
            st.markdown(href, unsafe_allow_html=True)
    else:
        st.warning("선택한 스타일과 색상 톤에 맞는 이미지가 없습니다.")
