### Work Log

### Update 11/11

Today I began the project. Firstly, I want to build the data fetcher using the football-data.org API. 
I created a config.py file to store the API key and the desired URL. Furthermore, I also created the data_fetch.py file to store the 
functions that will take care of the data collection. The idea is to have a module of functions (four as of now). Today, I solely worked
on the fetch_match_data() function. **I still have a lot of ground to cover while I familiarize myself with the API**. 
The two .txt files are output files that will help me better understand how the API requests works and how to configure the parse_data() function. 

### Update 21/11

Second day of working in the project. Today, I learned how to make API requests directly from the terminal. This will be much more efficient when it comes to trying out new things
with the API before actually writing any script. I have left some instructions on how to do this in the *config.py* file in case I forget.
After doing this, I requested the information for matchday 12 of LaLiga, and analyzed the JSON Object (another concept I have learned about today). This requests contain all the data that I
need to start building the CSV file to contain the information. Now, I need only to build a *parse_function()* that is actually able to correctly do this. 

I think it should have a structure similar to this one:
for every element in the array of the key "matches" 
    determine matchday
    find hometeam and awayteam
    find fulltime and halftime
        store goal scores in variables 
    put this values in the respective teams csv 

Next time I will do some more work on this

