import os 

# Retrieve the API key from the environment variable
FOOTBALL_API_KEY = os.getenv('FOOTBALL_DATA_API_KEY')

# API endpoint URL for fetching La Liga match data
ENDPOINT_URL = 'https://api.football-data.org/v4/competitions/PD/matches?matchday=12'

# Path to the CSV file where match data will be stored
STORAGE_FILE = 'data/laliga_matches.csv'

# Code I got in the email for launching
headers = { 'X-Auth-Token': FOOTBALL_API_KEY }
