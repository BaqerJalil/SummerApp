import streamlit as st
from shared.navbar import render_navbar
import pydeck as pdk

st.set_page_config(page_title="Map", page_icon="🗺️")
render_navbar()

st.title("🗺️ Explore Map")
st.markdown("Select what you're looking for:")

food = st.checkbox("🍔 Food")
events = st.checkbox("🎉 Events")
attractions = st.checkbox("📸 Attractions")

# (Optional) Example map
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/streets-v11',
    initial_view_state=pdk.ViewState(
        latitude=45.0,
        longitude=-70.0,
        zoom=4,
        pitch=50,
    )
))
