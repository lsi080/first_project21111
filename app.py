import streamlit as st
import random

st.title("💖 이상형 동물상 진단기")

st.write("""
좋아하는 사람이나 연예인의 사진을 5장 이상 업로드해주세요.  
사진을 분석해 당신의 이상형 동물상을 추천해드립니다!
""")

uploaded_files = st.file_uploader(
    "최소 5장 이상의 이미지를 업로드하세요",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=True
)

animal_types = {
    "강아지상": "친근하고 따뜻하며 충성심이 강한 유형",
    "고양이상": "독립적이고 신비로운 매력을 가진 유형",
    "사자상": "리더십 있고 당당하며 용감한 유형",
    "여우상": "교활하면서도 매혹적인 유형",
    "토끼상": "순수하고 귀여우며 상냥한 유형",
    "부엉이상": "지혜롭고 신중한 유형"
}

if uploaded_files:
    if len(uploaded_files) < 5:
        st.warning("최소 5장 이상의 이미지를 업로드해주세요!")
    else:
        st.success(f"{len(uploaded_files)}장의 사진이 업로드 되었습니다.")

        # (실제로는 이미지 분석하는 코드 필요, 여기선 랜덤 추천으로 대체)
        result = random.choice(list(animal_types.items()))

        st.subheader(f"🦄 당신의 이상형 동물상은 **{result[0]}** 입니다!")
        st.write(result[1])

        st.write("---")
        st.write("업로드된 이미지 미리보기:")
        for img_file in uploaded_files:
            st.image(img_file, width=150)
