import requests
import time
import pandas as pd

API_KEY = '5ae2e3f221c38a28845f05b65ab4c5efdc2a81e78fa6d872ea245bd9'
ENDPOINT = 'https://api.opentripmap.com/0.1/en/places/radius'

# Parameters (example for Portland, ME)
PARAMS = {
    'apikey': API_KEY,
    'radius': 1000,
    'limit': 50,
    'rate': 3,
    'format': 'json',
    'lon': -70.2553,  # Portland, ME longitude
    'lat': 43.6615,   # Portland, ME latitude
}

all_places = []
offset = 0
MAX_RESULTS = 2000

while len(all_places) < MAX_RESULTS:
    # Update offset if API supports it, or adjust params accordingly
    PARAMS['offset'] = offset

    response = requests.get(ENDPOINT, params=PARAMS)

    if response.status_code == 200:
        places = response.json()
        if not places:
            print("No more places found.")
            break

        # Add places to all_places list
        all_places.extend(places)
        print(f"Fetched {len(places)} places (total: {len(all_places)})")

        offset += len(places)
        time.sleep(0.5)  # Be polite to API
    else:
        print(f"Error fetching place list: {response.status_code} - {response.text}")
        break

# Optionally, you can clean or process data here
# Example: create DataFrame and save to CSV
df = pd.DataFrame(all_places)
df.to_csv('opentrip_places.csv', index=False)

print(f"✅ Total places fetched: {len(all_places)}")
print("Saved all data to 'opentrip_places.csv'")
