import streamlit as st
st.title('My First Streamlit App')
st.write('Welcome to my Streamlit app!')
user_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')
st.write('Customized Message:', user_input)