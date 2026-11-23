import streamlit as st

st.title("Student Performance Prediction System")
st.write("Hello! My first Streamlit app is working.")

name = st.text_input("Enter your name")

if st.button("Say Hello"):
    st.success("Hello, " + name + "! Welcome to my project.")