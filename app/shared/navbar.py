import streamlit as st

def render_navbar():
    col1, col2, col3 = st.columns([1, 8, 1])
    with col1:
        if st.button("🏠 Home"):
            st.switch_page("Home.py")
    with col3:
        if st.button("ℹ️ About"):
            st.switch_page("pages/4_About.py")
