import streamlit as st
from datetime import datetime

st.title("✨ 당신의 별자리와 그날 우주 이야기")

# 생년월일 입력
birth_date = st.date_input("생년월일을 선택하세요")

# 별자리 심볼 이미지 URL 딕셔너리 (무료 공개 이미지나 Unsplash, Wikimedia 등 사용 가능)
zodiac_images = {
    "물병자리 ♒️": "https://upload.wikimedia.org/wikipedia/commons/5/53/Aquarius.svg",
    "물고기자리 ♓️": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Pisces.svg",
    "양자리 ♈️": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Aries.svg",
    "황소자리 ♉️": "https://upload.wikimedia.org/wikipedia/commons/3/32/Taurus.svg",
    "쌍둥이자리 ♊️": "https://upload.wikimedia.org/wikipedia/commons/2/2c/Gemini.svg",
    "게자리 ♋️": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Cancer.svg",
    "사자자리 ♌️": "https://upload.wikimedia.org/wikipedia/commons/7/7c/Leo.svg",
    "처녀자리 ♍️": "https://upload.wikimedia.org/wikipedia/commons/6/68/Virgo.svg",
    "천칭자리 ♎️": "https://upload.wikimedia.org/wikipedia/commons/3/38/Libra.svg",
    "전갈자리 ♏️": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Scorpio.svg",
    "사수자리 ♐️": "https://upload.wikimedia.org/wikipedia/commons/6/68/Sagittarius.svg",
    "염소자리 ♑️": "https://upload.wikimedia.org/wikipedia/commons/3/30/Capricorn.svg",
}

def get_zodiac_sign(day, month):
    zodiac_dates = [
        ((1, 20), (2, 18), "물병자리 ♒️"),
        ((2, 19), (3, 20), "물고기자리 ♓️"),
        ((3, 21), (4, 19), "양자리 ♈️"),
        ((4, 20), (5, 20), "황소자리 ♉️"),
        ((5, 21), (6, 20), "쌍둥이자리 ♊️"),
        ((6, 21), (7, 22), "게자리 ♋️"),
        ((7, 23), (8, 22), "사자자리 ♌️"),
        ((8, 23), (9, 22), "처녀자리 ♍️"),
        ((9, 23), (10, 22), "천칭자리 ♎️"),
        ((10, 23), (11, 21), "전갈자리 ♏️"),
        ((11, 22), (12, 21), "사수자리 ♐️"),
        ((12, 22), (12, 31), "염소자리 ♑️"),
        ((1, 1), (1, 19), "염소자리 ♑️")
    ]
    for start, end, sign in zodiac_dates:
        start_month, start_day = start
        end_month, end_day = end
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            return sign
    return "별자리 정보 없음"

def get_universe_story(date):
    year = date.year
    events = {
        2023: "2023년, 우주에서는 거대한 목성 대적반의 색 변화가 관찰되었습니다.",
        2022: "2022년, 토성의 고리가 밝게 보이는 시기였습니다.",
        2021: "2021년, 화성 대접근으로 붉은 행성이 매우 선명히 보였죠.",
        2020: "2020년, 금성의 매우 밝은 모습이 밤하늘을 빛냈습니다."
    }
    return events.get(year, f"{year}년, 우주는 평소처럼 신비롭고 광활했습니다.")

if birth_date:
    day = birth_date.day
    month = birth_date.month
    sign = get_zodiac_sign(day, month)
    st.subheader(f"당신의 별자리는: {sign}")

    # 별자리 이미지 보여주기
    img_url = zodiac_images.get(sign)
    if img_url:
        st.image(img_url, width=200)
    else:
        st.write("별자리 이미지가 없습니다.")

    universe_story = get_universe_story(birth_date)
    st.write(f"📅 {birth_date}의 우주 이야기:")
    st.write(universe_story)
