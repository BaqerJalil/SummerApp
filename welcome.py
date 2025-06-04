import streamlit as st
from shared.navbar import render_navbar

st.set_page_config(page_title="Login", page_icon="🔐")
render_navbar()

st.title("🔐 Welcome / Login")
st.text_input("Username")
st.text_input("Password", type="password")

if st.button("Login"):
    st.switch_page("pages/2_Create_Trip.py")


