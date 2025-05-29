import requests
import time

API_KEY = 'iagcqPCvUum2pvST9aGOWqfCww730LAUHiv6gHkmWJFP2QgTV0umrXaZRRCshD2PUHPO0lI1zGSr-tc6vtxQai2hRo5IC2YTNJtOzARsJ7D1OdRpq4u-ollFt6gvaHYx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
}

PARAMS = {
    'term': 'restaurants',
    'location': 'Portland, ME',
    'limit': 50,  # Max allowed per request
}

all_businesses = []
offset = 0
MAX_RESULTS = 1000

while offset < MAX_RESULTS:
    PARAMS['offset'] = offset
    response = requests.get(ENDPOINT, headers=HEADERS, params=PARAMS)
    
    if response.status_code == 200:
        data = response.json()
        businesses = data.get('businesses', [])
        
        if not businesses:
            break  # No more results to fetch
        
        all_businesses.extend(businesses)
        offset += len(businesses)
        
        print(f"Fetched {len(businesses)} businesses (total: {len(all_businesses)})")
        time.sleep(0.5)  # Be polite to Yelp's servers
    else:
        print(f"Error: {response.status_code} - {response.text}")
        break

# Example: print names, ratings, and food types
for business in all_businesses:
    name = business.get('name')
    rating = business.get('rating')

    # Extract food types
    categories = business.get('categories', [])
    food_types = [category.get('title') for category in categories]

    # Extract address
    location = business.get('location', {})
    address = ", ".join(filter(None, location.get('display_address', [])))

    print(f"{name} - Rating: {rating} - Food Types: {', '.join(food_types)} - Address: {address}")

