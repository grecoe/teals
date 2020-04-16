'''
    Abstraction over data/drivers.csv

    Functionlity not complete, enough to get driver history.
'''

import os,sys,inspect

if __name__ == '__main__':
    # Fix path so we can import readers/base
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    base_directory = os.path.dirname(currentdir)
    os.chdir(base_directory)
    sys.path.insert(0,base_directory)

from f1readers.Driver import *
from f1readers.Races import *
from f1readers.Results import *
from f1readers.Status import *
from f1readers.Constructor import *
from app.utils.menuutils import MenuUtils
from app.utils.interface import IFunction
from app.f1functions.constants import F1DataConstants
from app.f1functions.driver_stats import DriverStats
from app.f1functions.driver_search import DriverSearch

# Example of how to implement the IFunction
from app.f1functions.dummy import DummyFunction

'''
    The IFunction base class expects a data set dictionary. Each
    class that derives from it will have access to the dataset
    dictionary internally. 

    Dictionary is built using F1DataConstants as keys so that 
    the keys remain constant across the F1Functions.
'''
f1_datasets = {
    F1DataConstants.DRIVER_DATA : DriverDataFile() ,
    F1DataConstants.RACE_DATA : RacesDataFile(),
    F1DataConstants.RESULTS_DATA : ResultsDataFile(),
    F1DataConstants.STATUS_DATA : StatusDataFile(),
    F1DataConstants.CONSTRUCTOR_DATA : ConstructorsDataFile()
}

def help():
    '''
        Top level help function
    '''
    MenuUtils.display_menu_help(app_functions)

def clear():
    '''
        Clear the screen
    '''
    os.system('cls')

def my_name():
    '''
        Who knows the reference?
    '''
    print("Heisenberg")


'''
    The applicaiton menu is built using a dictionary with string keys
    and end nodes are comprised of IFunction instances or actual functions
    in wich callable(fn) == True
'''
app_functions = {
    "get" : {
        "driver" : {
            "stats" : DriverStats(f1_datasets)
        },
        "constructor" : {
            "stats" : DummyFunction(f1_datasets)
        }
    },
    "list" : {
        "drivers" : DriverSearch(f1_datasets),
        "constructors" : DummyFunction(f1_datasets),
        "races" : DummyFunction(f1_datasets)
    },
    "say" : {
        "my" : {
            # Hahahahahahaha
            "name" : my_name
        }
    },
    "clear" : clear,
    "help" : help,
    "quit" : quit
}

'''
    Application loop

    Accept input from the user. Parse that input and try and find 
    an end node function or IFunction instance. Any additional parameters
    are then passed along as a list to IFunction instances only. 

    You will not have to change this code below, the only requirement to
    extend the functionality comes in the app_functions dictionary and 
    possibly the f1_datasets dictionary (assuming you extend the F1 Readers
    to a new CSV file that has not yet been implemented).
'''
while True:   
    user_input = input("F1 : > ")
    inputs = user_input.split(' ')

    if len(inputs) > 0 and inputs[0] in app_functions.keys():
        current_action = app_functions
        last_command_index = 0

        for next_input in inputs:
        
            next_input = next_input.strip()
            if len(next_input) == 0 :
                continue

            last_command_index += 1
            '''
                Note that on an invalid command, a high level function, or 
                an instance of IFunction, we want to break the loop once
                we execute that if/elif segment as there are no more items 
                to parse. 
            '''
            if next_input not in current_action.keys():
                print("Invalid Command : ", " ".join(inputs))
                MenuUtils.display_menu_help(app_functions)
                break
            elif callable(current_action[next_input]):
                # Top level functions, typically quit and help
                current_action[next_input]()
                break
            elif isinstance(current_action[next_input], IFunction):
                # IFunction instance
                current_action[next_input].execute(inputs[last_command_index:])
                break
            else:
                current_action = current_action[next_input]
    else:
        print("Invalid Command : ", " ".join(inputs))
        display_menu_help(menu_options, None)
