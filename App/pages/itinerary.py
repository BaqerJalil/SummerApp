import streamlit as st

st.set_page_config(page_title="Itinerary", layout="centered")

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
    h1, h2 {
        text-align: center;
        margin-top: 3rem;
        color: white;
    }
    .event-item {
        max-width: 600px;
        margin: 1rem auto;
        padding: 1rem;
        background-color: #111;
        border-radius: 8px;
        font-size: 1.1rem;
        border: 1px solid #333;
    }
</style>

<div class="custom-navbar">
    <div class="nav-link" id="about-link">About</div>
    <div class="nav-link" id="home-link">Home</div>
</div>
""", unsafe_allow_html=True)

st.title("Trip Itinerary")

query_params = st.query_params
trip_id = query_params.get("trip", [""])[0]

if trip_id == "testing-trip":
    st.header("Testing Trip Schedule")
    events = [
        {"date": "Jun 20, 2025", "event": "Visit Old Port"},
        {"date": "Jun 21, 2025", "event": "Lunch at Local Seafood"},
        {"date": "Jun 22, 2025", "event": "Boat Tour"},
    ]
    for ev in events:
        st.markdown(f'<div class="event-item"><strong>{ev["date"]}</strong> — {ev["event"]}</div>', unsafe_allow_html=True)
else:
    st.markdown('<div style="text-align:center; margin-top: 3rem;">No itinerary found for this trip.</div>', unsafe_allow_html=True)

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
