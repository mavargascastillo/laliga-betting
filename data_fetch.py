'''
Author: Miguel Ángel Vargas

Info: Web scraper that uses the football-data.org API to get information from LaLiga matches.
'''

import requests
import time
from config import ENDPOINT_URL, headers # config.py values

def fetch_match_data():
    params = {'season': '2021' , 'matchday': '23' } # Go over the API's documentation to see the exact code

    try:
        response = requests.get(ENDPOINT_URL, headers = headers, params = params)
        if response.status_code == 200:
            print(response)
            data = response.json()
            # goals_data = parse_goals_data(data) # Assumming we already have a Parse function.
            print(data)
            return data
        else:
            print(f"Error: {response.status_code}")
    except requests.RequestException as e:
        print("Network error:", e)
        return None

datos = fetch_match_data()