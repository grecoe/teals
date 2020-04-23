'''
    Formula 1 app
'''

'''
    Ensure that path is pointing all the way up to 6_DeepProjects. If 
    moved from this location, you will need to ensure you correct the path.
'''
import os
import sys
import inspect

core_directory = '6_DeepProjects'
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

dir_split = os.path.split(currentdir)
while dir_split[1] != core_directory:
    currentdir = dir_split[0]
    dir_split = os.path.split(currentdir)
# Now that we have the core directory, we can now start importing 
# what we need once we set the path. 
sys.path.insert(0,currentdir)

# Now that the path is set to the top folder where we can get at 
# Utilities needed, reference every package from there.

# General Utilties
from multi_command_utils.multi_command_application import MultiCommandApp
from multi_command_utils.interface_dummy import DummyFunction

# Formula 1 Data Readers
from Formula1.f1_data_readers.Driver import *
from Formula1.f1_data_readers.DriverStanding import *
from Formula1.f1_data_readers.Races import *
from Formula1.f1_data_readers.Results import *
from Formula1.f1_data_readers.Status import *
from Formula1.f1_data_readers.Constructor import *

# Formula One Functions
from Formula1.f1_functions.constants import F1DataConstants
from Formula1.f1_functions.driver_stats import DriverStats
from Formula1.f1_functions.driver_standings import DriverStandings
from Formula1.f1_functions.driver_search import DriverSearch
from Formula1.f1_functions.list_races import ListRaces

'''
from multi_command_utils.data_file import column_data

race_file = RacesDataFile()
driver_standing = DriverStandingFile()
senna_standings = []
races = race_file.get_by_race_year('2015')

race = races[-1]
standings = driver_standing.find([column_data('raceId', race.raceId)])
for standing in standings:
    standing.points = int(standing.points)

print(len(standings))
standings = sorted(standings, reverse=True, key=lambda standing : standing.points)
for standing in standings:
    print(standing.driverId, standing.points)

quit()
print(standings[0].driverId, standings[0].points)
standings = driver_standing.find([column_data('position', '2'), column_data('raceId', race.raceId)])
print(standings[0].driverId, standings[0].points)
standings = driver_standing.find([column_data('position', '3'), column_data('raceId', race.raceId)])
print(standings[0].driverId, standings[0].points)
quit()

for race in races:
    standings = driver_standing.find([column_data('driverId', '102'), column_data('raceId', race.raceId)])
    senna_standings.append(standings[0])
print(len(races))
for ss in senna_standings:
    print(ss.raceId, ss.points, ss.position)
quit()
'''

'''
    The IFunction base class expects a data set dictionary. Each
    class that derives from it will have access to the dataset
    dictionary internally. 

    Dictionary is built using F1DataConstants as keys so that 
    the keys remain constant across the F1Functions.
'''
f1_datasets = {
    F1DataConstants.DRIVER_DATA : DriverDataFile() ,
    F1DataConstants.DRIVER_STANDING_DATA : DriverStandingFile(),
    F1DataConstants.RACE_DATA : RacesDataFile(),
    F1DataConstants.RESULTS_DATA : ResultsDataFile(),
    F1DataConstants.STATUS_DATA : StatusDataFile(),
    F1DataConstants.CONSTRUCTOR_DATA : ConstructorsDataFile()
}

'''
    The applicaiton menu is built using a dictionary with string keys
    and end nodes are comprised of IFunction instances or actual functions
    in wich callable(fn) == True
'''
app_functions = {
    "get" : {
        "driver" : {
            "stats" : DriverStats(f1_datasets),
            "standings" : DriverStandings(f1_datasets)

        },
        "constructor" : {
            "stats" : DummyFunction(f1_datasets)
        }
    },
    "list" : {
        "drivers" : DriverSearch(f1_datasets),
        "races" : ListRaces(f1_datasets),
        "constructors" : DummyFunction(f1_datasets)
    }
}


app = MultiCommandApp("F1", app_functions)
app.run()