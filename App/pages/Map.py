import streamlit as st
import pydeck as pdk

st.set_page_config(page_title="Explore Map", page_icon=None, layout="centered")

st.markdown("""
<style>
    body, .main {
        background-color: #000;
        color: white;
        font-family: Arial, sans-serif;
    }
    .custom-navbar {
        background-color: #111;
        padding: 0.4rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #333;
        font-family: sans-serif;
    }
    .nav-link {
        color: white;
        text-decoration: none;
        padding: 6px 14px;
        border: 1px solid #333;
        border-radius: 6px;
        font-size: 15px;
        font-weight: 500;
        user-select: none;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    .nav-link:hover {
        background-color: #222;
        border-color: #555;
    }
    label[data-baseweb="checkbox"] {
        color: white;
        font-weight: 600;
        font-size: 16px;
    }
    h1, h2 {
        text-align: center;
        margin-top: 3rem;
        color: white;
    }
    .stCheckbox > div {
        padding-bottom: 0.4rem;
    }
</style>

<div class="custom-navbar">
    <div class="nav-link" id="about-link">About</div>
    <div class="nav-link" id="home-link">Home</div>
</div>
""", unsafe_allow_html=True)

st.title("Explore Map")
st.markdown("Select what you're looking for:")

food = st.checkbox("Food")
events = st.checkbox("Events")
attractions = st.checkbox("Attractions")

PORTLAND_LAT = 43.6591
PORTLAND_LON = -70.2568

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/dark-v10',
    initial_view_state=pdk.ViewState(
        latitude=PORTLAND_LAT,
        longitude=PORTLAND_LON,
        zoom=12,
        pitch=45,
    ),
    layers=[],
))

st.markdown("""
<script>
    function navigateTo(page) {
        const url = new URL(window.location);
        url.searchParams.set('page', page);
        window.history.pushState({}, '', url);
        window.location.reload();
    }
    document.getElementById('about-link').onclick = () => navigateTo('about');
    document.getElementById('home-link').onclick = () => navigateTo('home');
</script>
""", unsafe_allow_html=True)
