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