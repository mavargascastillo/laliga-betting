# laliga-betting
Second repository dedicated to build an automated betting strategy for LaLiga matches.

### Update 11/11

Today I began the project. Firstly, I want to build the data fetcher using the football-data.org API. 
I created a config.py file to store the API key and the desired URL. Furthermore, I also created the data_fetch.py file to store the 
functions that will take care of the data collection. The idea is to have a module of functions (four as of now). Today, I solely worked
on the fetch_match_data() function. **I still have a lot of ground to cover while I familiarize myself with the API**. 
The two .txt files are output files that will help me better understand how the API requests works and how to configure the parse_data() function. 
