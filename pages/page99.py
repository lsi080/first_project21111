import streamlit as st
import hashlib

def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

st.title("🔐 암호화 체험 웹앱")
st.write("고전암호(시저)와 현대 해시(SHA256)를 직접 입력해보고 비교해보세요!")

input_text = st.text_input("암호화할 텍스트를 입력하세요:")
method = st.selectbox("암호화 방식 선택", ["시저 암호", "SHA256 해시"])

if method == "시저 암호":
    shift = st.slider("시프트 값 선택 (1~25)", 1, 25, 3)
    encrypted_text = caesar_encrypt(input_text, shift)
    decrypted_text = caesar_decrypt(encrypted_text, shift)

    st.subheader("🔐 암호문:")
    st.code(encrypted_text)
    st.subheader("🔓 복호화 결과:")
    st.code(decrypted_text)

elif method == "SHA256 해시":
    hashed_text = sha256_hash(input_text)
    st.subheader("🔐 해시 결과 (복호화 불가능):")
    st.code(hashed_text)
    st.info("SHA256은 단방향 해시 함수이므로 복호화할 수 없습니다.")
