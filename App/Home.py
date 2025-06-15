import streamlit as st

st.set_page_config(page_title="Home", page_icon=None, layout="centered")

st.markdown("""
<style>
    body, .main {
        background-color: #000;
        color: white;
        font-family: Arial, sans-serif;
    }
    .custom-navbar {
        background-color: #111;
        padding: 10px 30px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #333;
        font-weight: 600;
        font-size: 16px;
        user-select: none;
    }
    .nav-link {
        color: white;
        text-decoration: none;
        padding: 8px 16px;
        border: 1px solid #333;
        border-radius: 6px;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    .nav-link:hover {
        background-color: #222;
        border-color: #555;
    }
    h3#welcome {
        text-align: center;
        font-weight: 700;
        font-size: 3.5rem;
        margin-bottom: 20px;
        color: #ccc;
    }
    p.instructions {
        text-align: center;
        color: #bbb;
        margin-bottom: 40px;
        font-size: 1.2rem;
    }
    .login-box {
        max-width: 400px;
        margin: 0 auto;
        padding: 0 10px;
    }
    .stTextInput>div>div>input {
        background-color: #111 !important;
        color: white !important;
        border-radius: 6px;
        border: 1px solid #333;
        padding: 10px;
    }
    .stTextInput>div>label {
        font-weight: 600;
        font-size: 16px;
        margin-top: 12px;
        color: #ddd;
    }

    /* Button container spacing */
    .stButton {
        display: inline-block;
        margin-right: 12px;
        margin-bottom: 12px;
    }

    /* Button style */
    .stButton > button {
        min-width: 140px;
        height: 32px;
        padding: 0 20px;
        line-height: 32px;
        background-color: #222;
        color: white;
        border: 1px solid #555;
        border-radius: 6px;
        cursor: pointer;
        user-select: none;
        font-weight: 600;
        font-size: 16px;
        transition: background-color 0.2s;
    }
    .stButton > button:hover {
        background-color: #444;
        border-color: #888;
    }
</style>

<div class="custom-navbar">
    <div class="nav-link" id="about-link">About</div>
    <div class="nav-link" id="home-link">Home</div>
</div>

<h3 id="welcome">Welcome</h3>
<p class="instructions">Please log in below:</p>

<div class="login-box">
""", unsafe_allow_html=True)

username = st.text_input("Username", placeholder="Enter your username")
password = st.text_input("Password", placeholder="Enter your password", type="password")

# Buttons side by side
col1, col2 = st.columns(2)
with col1:
    if st.button("Enter"):
        st.experimental_set_query_params(page="newtrip")
        st.experimental_rerun()
with col2:
    if st.button("Cancel"):
        st.experimental_set_query_params(page="home")
        st.experimental_rerun()

st.markdown("</div>", unsafe_allow_html=True)

# JavaScript for navbar links
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
