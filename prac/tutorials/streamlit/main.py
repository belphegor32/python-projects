import streamlit as st
import os

st.title("Super simple title")
st.header("This is a header")
st.subheader("Subheader")
st.markdown("This is a **Markdown**")
st.caption("Small text")

code_example = """
def greet(name):
    print('hello', name)
"""
st.code(code_example, language="python")

st.divider()

st.image(os.path.join(os.getcwd(), "static", "BG.jpg"))