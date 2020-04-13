# Formula 1

Explore Formula 1 Data from 1950 - 2017

Data Provided by kaggle.com : https://www.kaggle.com/cjgdev/formula-1-race-data-19502017

This project allows you to program interesting information about Formula 1 over many years. The starter program shows how to pull together the differnt files to get interesting information.

There are two examples in this repo. One that uses the data files that are read in using readers/base.py (starter.py) and another that wraps DataReader from readers/base.py in specific classes (custom/*). 

Both solutions follow a similar path  :
- Look up a driver by first and last name
- Retrieve all of their race history
- Print an overview of their Formula 1 history

### Example Output from either solution
Calling the code as provided will give your information about Alberto Ascari, his history and his race results as:

Alberto Ascari Results:

Years In F1 : 6

Grands Prix : 36

Front Rows  : 21 of which 14 are pole position

Podiums     : 17

DNF Total   : 14

RESULTS:

|YEAR|ROUND|GRID|FINISH|STATUS|NAME|
|--|--|--|--|--|--|
|1950|2|7|2|+1 Lap|Monaco Grand Prix|
|1950|4|5|DNF|Oil pump|Swiss Grand Prix|
|1950|5|7|5|+1 Lap|Belgian Grand Prix|


## What you can do
### starter.py or abstract.py
Use the templates and some creativity and add more funcitonality
- What constructor did the driver drive for each race? (constructors.csv)
- What was the drivers standing in the drivers championship for each race? (driverStandings.csv)
- What was the constructors standing in the constructors championship for each race? (constructorStandings.csv)
- If the driver qualified for pole position, what was the fastest lap in q3?) (qualifying.csv)?
- Use your imagination and come up with something interesting.  
#### abstract.py
- If extending the abstract.py you will need to add classes to custom/* for any new files you include. Follow the templates laid out in the custom/ directory. See if you can figure it out!

<B>NOTE<B> These are simply suggestions, get creative and explore the data. 

## Complex multi argument implementation
A much more complex and complete solution for an application can be found in the app/ directory. That folder contains it's own readme file to walk you through it and get you started with it. 

## Getting Started
1. Clone this repository to you laptop
2. Unzip the formula-1-race-data-19502017.zip file to a directory called /data
3. Run the starter.py file to see some results. 
4. Run the abstract.py file to see some results. 
