import streamlit as st

st.title("Hello! Streamlit App")

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
