import os 

# Retrieve the API key from the environment variable
FOOTBALL_API_KEY = os.getenv('FOOTBALL_DATA_API_KEY')

# API endpoint URL for fetching La Liga match data
ENDPOINT_URL = 'https://api.football-data.org/v4/competitions/PD/matches?matchday=12'

# Path to the CSV file where match data will be stored
STORAGE_FILE = 'data/laliga_matches.csv'

# Code I got in the email for launching
headers = { 'X-Auth-Token': FOOTBALL_API_KEY }

# This is some information on how to interact with the API directly from the terminal:
# export API_KEY="YOUR_API_KEY" -> this is to set up an environment variable so I do not need to write every single time the auth token in the terminal
# curl -X GET "https://api.football-data.org/v4/competitions" -H "X-Auth-Token: $API_KEY"


