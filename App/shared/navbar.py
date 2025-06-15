import streamlit as st
from streamlit_extras.switch_page_button import switch_page

def render_navbar():
    st.markdown("""
        <style>
            .custom-navbar {
                background-color: #111;
                padding: 10px 30px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-bottom: 1px solid #333;
                font-family: Arial, sans-serif;
            }
            .nav-button {
                background-color: #111 !important;
                color: white !important;
                border: 1px solid #333 !important;
                border-radius: 6px !important;
                font-weight: 600 !important;
                padding: 8px 16px !important;
                font-size: 15px !important;
            }
            .nav-button:hover {
                background-color: #222 !important;
                border-color: #555 !important;
            }
        </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("About", use_container_width=True):
            switch_page("About")
    with col2:
        if st.button("Home", use_container_width=True):
            switch_page("Home")
