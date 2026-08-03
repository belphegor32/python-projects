import streamlit as st

if "slider" not in st.session_state:
    st.session_state.slider = 25

min_value = st.slider("Set min value", 0, 50, 25)

st.session_state.slider = st.slider("Slider", min_value, 100, st.session_state.slider)