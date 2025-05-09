import requests

BASE_URL = 'https://world.openfoodfacts.org'

def search_product(query: str) -> dict:
    url = f"{BASE_URL}/cgi/search.pl"
    params = {
        'search_terms': query,
        'search_simple': 1,
        'action': 'process',
        'json': 1
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': response.text}
