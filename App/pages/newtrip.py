import streamlit as st

st.set_page_config(page_title="Trips", layout="centered")

html = """
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
        user-select: none;
        font-weight: 600;
        font-size: 16px;
    }
    .nav-link {
        color: white;
        text-decoration: none;
        padding: 8px 16px;
        border: 1px solid #333;
        border-radius: 6px;
        transition: background-color 0.2s;
        cursor: pointer;
    }
    .nav-link:hover {
        background-color: #222;
        border-color: #555;
    }
    h1 {
        text-align: center;
        margin-top: 40px;
        margin-bottom: 40px;
    }
    .trips-container {
        background-color: #111;
        border: 1px solid #333;
        border-radius: 8px;
        max-width: 900px;
        margin: 0 auto 60px auto;
        padding: 20px 30px 30px 30px;
        position: relative;
        min-height: 300px;
        box-sizing: border-box;
    }
    .trip-row {
        background-color: #222;
        padding: 14px 20px;
        margin-bottom: 14px;
        border-radius: 6px;
        cursor: pointer;
        font-size: 18px;
        font-weight: 600;
        transition: background-color 0.2s ease;
        user-select: none;
    }
    .trip-row:hover {
        background-color: #333;
    }
    .plus-button {
        position: absolute;
        top: -18px;        /* Adjusted */
        right: -18px;      /* Adjusted */
        background-color: #222;
        color: white;
        border: 1px solid #555;
        border-radius: 50%;
        width: 38px;
        height: 38px;
        font-size: 28px;
        font-weight: bold;
        cursor: pointer;
        line-height: 34px;
        text-align: center;
        user-select: none;
        transition: background-color 0.2s ease;
        box-shadow: 0 0 6px rgba(0,0,0,0.6);
    }
    .plus-button:hover {
        background-color: #444;
        border-color: #888;
    }
</style>

<div class="custom-navbar">
    <div class="nav-link" onclick="navigatePage('about')">About</div>
    <div class="nav-link" onclick="navigatePage('home')">Home</div>
</div>

<h1>Trips</h1>

<div class="trips-container">
    <div class="plus-button" id="plus-btn" title="Create New Trip">+</div>
    <div class="trip-row" data-tripid="testing-trip">Testing Trip</div>
    <!-- Add more trips here -->
</div>

<script>
    function navigatePage(page) {
        const url = new URL(window.location);
        url.searchParams.set('page', page);
        url.searchParams.delete('trip');
        window.history.pushState({}, '', url);
        window.location.reload();
    }

    document.querySelectorAll('.trip-row').forEach(row => {
        row.addEventListener('click', () => {
            const tripId = row.getAttribute('data-tripid');
            const url = new URL(window.location);
            url.searchParams.set('page', 'itinerary');
            url.searchParams.set('trip', tripId);
            window.history.pushState({}, '', url);
            window.location.reload();
        });
    });

    document.getElementById('plus-btn').addEventListener('click', () => {
        const url = new URL(window.location);
        url.searchParams.set('page', '3_Map');
        url.searchParams.delete('trip');
        window.history.pushState({}, '', url);
        window.location.reload();
    });
</script>
"""

st.markdown(html, unsafe_allow_html=True)
