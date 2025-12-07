import streamlit as st

st.title("サンプルアプリ２")
st.write("これは Streamlit のデプロイ練習用アプリです！")

text = st.text_input("お名前を入力してください")
if text:
    st.write(f"{text} さん、こんにちは！")
