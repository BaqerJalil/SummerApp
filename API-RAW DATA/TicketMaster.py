import requests
import pandas as pd

# API setup
API_KEY = "jrT33giRPXb5Gq8c8NU2pQXD5ANxLXrw"
url = "https://app.ticketmaster.com/discovery/v2/events.json"

params = {
    "apikey": API_KEY,
    "city": "Portland",
    "stateCode": "ME",
    "countryCode": "US",
    "size": 50,
    "sort": "date,asc"
}

response = requests.get(url, params=params)
data = response.json()

# Extract event data
events = data.get('_embedded', {}).get('events', [])

raw_data = []
for event in events:
    raw_data.append({
        "name": event.get("name"),
        "date": event.get("dates", {}).get("start", {}).get("localDate"),
        "time": event.get("dates", {}).get("start", {}).get("localTime"),
        "venue": event.get("_embedded", {}).get("venues", [{}])[0].get("name"),
        "url": event.get("url")
    })

# Convert to DataFrame
df_raw = pd.DataFrame(raw_data)

# Save raw version
df_raw.to_csv("ticketmaster_raw.csv", index=False)

# Cleaned version
df_cleaned = df_raw.copy()

# Normalize: lowercase and strip text
for col in ["name", "venue", "url"]:
    df_cleaned[col] = df_cleaned[col].astype(str).str.lower().str.strip()

# Handle missing values
df_cleaned.fillna("missing", inplace=True)

# Save cleaned version
df_cleaned.to_csv("ticketmaster_cleaned.csv", index=False)

print("✅ Raw and cleaned event data saved as CSV files.")
