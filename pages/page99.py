# Streamlit과 hashlib 라이브러리 불러오기
import streamlit as st
import hashlib

# 시저 암호 암호화 함수
def caesar_encrypt(text, shift):
    encrypted = ""  # 암호문 저장 변수
    for char in text:
        if char.isalpha():  # 알파벳인 경우만 암호화
            offset = 65 if char.isupper() else 97  # 대소문자 구분
            # 아스키 코드를 이용해 시프트 연산 (A~Z or a~z 사이에서 순환)
            encrypted += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            # 알파벳이 아니면 그대로 추가 (공백, 숫자, 기호 등)
            encrypted += char
    return encrypted

# 시저 암호 복호화 함수 (시프트 값을 음수로 줘서 암호 해제)
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# SHA256 해시 함수 (복호화 불가능한 단방향 암호)
def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Streamlit 웹앱 제목 및 설명
st.title("🔐 암호화 체험 웹앱")
st.write("고전암호(시저)와 현대 해시(SHA256)를 직접 입력해보고 비교해보세요!")

# 사용자로부터 입력 받을 평문 텍스트
input_text = st.text_input("암호화할 텍스트를 입력하세요:")

# 암호화 방식 선택 (시저 암호 또는 SHA256 해시)
method = st.selectbox("암호화 방식 선택", ["시저 암호", "SHA256 해시"])

# 시저 암호 선택 시
if method == "시저 암호":
    # 시프트 값 슬라이더로 입력 (1~25)
    shift = st.slider("시프트 값 선택 (1~25)", 1, 25, 3)
    
    # 암호화 및 복호화 수행
    encrypted_text = caesar_encrypt(input_text, shift)
    decrypted_text = caesar_decrypt(encrypted_text, shift)

    # 결과 출력
    st.subheader("🔐 암호문:")
    st.code(encrypted_text)

    st.subheader("🔓 복호화 결과:")
    st.code(decrypted_text)

# SHA256 해시 선택 시
elif method == "SHA256 해시":
    # 해시 처리
    hashed_text = sha256_hash(input_text)

    # 결과 출력 (복호화 불가능)
    st.subheader("🔐 해시 결과 (복호화 불가능):")
    st.code(hashed_text)
    st.info("SHA256은 단방향 해시 함수이므로 복호화할 수 없습니다.")
