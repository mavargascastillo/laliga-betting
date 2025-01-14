import csv
import json

# Define the input and output file paths
txt_file_path = "output3.txt"
csv_file_path = "matches.csv"

def extract_matchday(data):
    """
    Extract the matchday from the main JSON data.
    """
    return data.get("filters", {}).get("matchday", None)

def safe_get(value, placeholder="N/A"):
    """
    Safely return a value, defaulting to a placeholder if None.
    """
    return value if value is not None else placeholder

def extract_match_data(match):
    """
    Extract match data from a single match dictionary.
    Returns a dictionary with team names as keys and their goals by half as values.
    """
    home_team = match['homeTeam']['name']
    away_team = match['awayTeam']['name']
    half_time_home_goals = safe_get(match['score']['halfTime'].get('home'))
    half_time_away_goals = safe_get(match['score']['halfTime'].get('away'))
    full_time_home_goals = safe_get(match['score']['fullTime'].get('home'))
    full_time_away_goals = safe_get(match['score']['fullTime'].get('away'))
    
    return {
        home_team: {"First Half": half_time_home_goals, "Second Half": full_time_home_goals},
        away_team: {"First Half": half_time_away_goals, "Second Half": full_time_away_goals},
    }

def process_matches(txt_file_path, csv_file_path):
    """
    Process the matches from the .txt file and write them to the .csv file.
    """
    try:
        with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
            # Read the entire file as a JSON object
            data = json.load(txt_file)
            
            # Extract the matchday and matches
            matchday = extract_matchday(data)
            matches = data.get('matches', [])
            
            # Collect all team data for the matchday
            matchday_data = {}
            for match in matches:
                match_data = extract_match_data(match)
                for team, goals in match_data.items():
                    if team not in matchday_data:
                        matchday_data[team] = {"First Half": 0, "Second Half": 0}
                    # Add values only if they are numeric
                    if isinstance(goals["First Half"], int):
                        matchday_data[team]["First Half"] += goals["First Half"]
                    if isinstance(goals["Second Half"], int):
                        matchday_data[team]["Second Half"] += goals["Second Half"]
            
            # Write data to CSV
            write_to_csv(matchday, matchday_data, csv_file_path)
    except Exception as e:
        print(f"Error processing matches: {e}")

def write_to_csv(matchday, matchday_data, csv_file_path):
    """
    Write or append matchday data to a CSV file.
    """
    try:
        # Prepare headers: each team will have two sub-columns
        teams = sorted(matchday_data.keys())  # Alphabetical order for consistent structure
        headers = []
        for team in teams:
            headers.append(f"{team} (First Half)")
            headers.append(f"{team} (Second Half)")
        
        # Prepare the matchday row
        row = []
        for team in teams:
            row.append(matchday_data[team]["First Half"])
            row.append(matchday_data[team]["Second Half"])
        
        # Check if the file exists and write data accordingly
        with open(csv_file_path, mode='a+', newline='', encoding='utf-8') as csv_file:
            csv_file.seek(0)
            csv_reader = csv.reader(csv_file)
            existing_headers = next(csv_reader, None)
            
            if not existing_headers:
                # Write headers if the file is empty
                csv_file.seek(0)
                csv_file.truncate()
                writer = csv.writer(csv_file)
                writer.writerow(["Matchday"] + headers)
            
            # Write matchday data
            writer = csv.writer(csv_file)
            writer.writerow([matchday] + row)
    except Exception as e:
        print(f"Error writing to CSV: {e}")

# Run the script
process_matches(txt_file_path, csv_file_path)
