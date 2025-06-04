import streamlit as st
from shared.navbar import render_navbar

st.set_page_config(page_title="About", page_icon="ℹ️")
render_navbar()

st.title("ℹ️ About")
st.markdown("""
This app helps you plan trips by selecting attractions, events, and food spots on a map.

Built with ❤️ using Streamlit.
""")
