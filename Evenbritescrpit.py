import requests
import time

API_TOKEN = 'YOUR_EVENTBRITE_API_TOKEN'  # Replace with your actual token
ENDPOINT = 'https://www.eventbriteapi.com/v3/events/search/'

HEADERS = {
    'Authorization': f'Bearer {API_TOKEN}',
}

PARAMS = {
    'location.address': 'Portland, ME',
    'expand': 'venue',       # Optional: expands venue data in results
    'page': 1,               # Start on page 1
    'page_size': 50,         # Max page size allowed
}

all_events = []
MAX_PAGES = 20  # 20 pages * 50 = 1000 events max

while PARAMS['page'] <= MAX_PAGES:
    response = requests.get(ENDPOINT, headers=HEADERS, params=PARAMS)
    
    if response.status_code == 200:
        data = response.json()
        events = data.get('events', [])
        
        if not events:
            break
        
        all_events.extend(events)
        print(f"Fetched {len(events)} events (total: {len(all_events)})")
        
        if not data['pagination']['has_more_items']:
            break  # Stop if no more pages
        PARAMS['page'] += 1
        time.sleep(0.5)
    else:
        print(f"Error: {response.status_code} - {response.text}")
        break

# Print example output
for event in all_events:
    name = event['name']['text']
    start = event['start']['local']
    venue = event.get('venue', {}).get('address', {}).get('localized_address_display', 'No venue info')
    print(f"{name} - Start: {start} - Venue: {venue}")
