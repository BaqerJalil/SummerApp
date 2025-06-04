import streamlit as st
import sys
import os

# Add parent folder to sys.path so shared module can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'shared')))
from navbar import render_navbar

st.set_page_config(page_title="Home", page_icon="🏠", layout="centered")

render_navbar()

st.title("🏠 Home Page")
st.markdown("""
Welcome! Start your journey by heading to the login page.
""")

if st.button("🔐 Go to Login"):
    st.experimental_set_query_params(page="login")  # or use switch_page if you have it
    st.experimental_rerun()
