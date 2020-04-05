import requests
import json

from auth import cat_api_key

def get_random_cat_url ():
    response = requests.get("https://api.thecatapi.com/v1/images/search", headers = {"x-api-key" : cat_api_key})
    data = response.json()
    url = data[0]['url']
    return url