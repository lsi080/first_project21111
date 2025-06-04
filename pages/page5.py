import streamlit as st
import requests
import json

# OpenWeatherMap API 키
API_KEY = '7b539cee9a0958d43ab5eb510b97843b'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    """주어진 도시의 날씨 정보를 API로 가져오기"""
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric&lang=kr"  # 'metric'으로 섭씨 온도
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        description = weather['description']
        return {
            "temperature": temperature,
            "pressure": pressure,
            "humidity": humidity,
            "description": description,
        }
    else:
        return None

def show_weather():
    """Streamlit 앱의 메인 인터페이스"""
    st.title("날씨 정보 앱")
    st.write("특정 지역의 날씨를 확인하세요.")

    city = st.text_input("도시 이름을 입력하세요 (예: 서울):")
    
    if city:
        weather = get_weather(city)
        
        if weather:
            st.write(f"### {city}의 날씨")
            st.write(f"기온: {weather['temperature']}°C")
            st.write(f"습도: {weather['humidity']}%")
            st.write(f"기압: {weather['pressure']} hPa")
            st.write(f"날씨 설명: {weather['description']}")
        else:
            st.error("잘못된 도시 이름입니다. 다시 시도해 주세요.")

if __name__ == "__main__":
    show_weather()
