import streamlit as st
from shared.navbar import render_navbar

st.set_page_config(page_title="Create Trip", page_icon="🧳")
render_navbar()

st.title("🧳 Create New Trip")
st.text_input("Trip Name")
st.date_input("Start Date")
st.date_input("End Date")

if st.button("Next: Choose Attractions"):
    st.switch_page("pages/3_Map.py")
