import streamlit as st

st.set_page_config(page_title="About", page_icon=None, layout="centered")

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
    h1 {
        text-align: center;
        margin-top: 3rem;
        color: white;
    }
    .content {
        max-width: 600px;
        margin: 2rem auto;
        font-size: 1.2rem;
        color: #ccc;
        line-height: 1.6;
    }
</style>

<div class="custom-navbar">
    <div class="nav-link" id="about-link">About</div>
    <div class="nav-link" id="home-link">Home</div>
</div>
""", unsafe_allow_html=True)

st.title("About")

st.markdown("""
<div class="content">
    Why do need me to tell you what this is. Anyways did you know lebron james is the first player hit every point milestone. goat stuff
</div>
""", unsafe_allow_html=True)

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
