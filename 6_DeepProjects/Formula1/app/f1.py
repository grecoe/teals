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

from custom.Driver import *
from custom.Races import *
from custom.Results import *
from custom.Status import *
from custom.Constructor import *
from app.functions.interface import IFunction
from app.functions.dummy import DummyFunction
from app.utils.menuutils import MenuUtils

f1_datasets = {
    IFunction.DRIVER_DATA : DriverDataFile() ,
    IFunction.RACE_DATA : RacesDataFile(),
    IFunction.RESULTS_DATA : ResultsDataFile(),
    IFunction.STATUS_DATA : StatusDataFile(),
    IFunction.CONSTRUCTOR_DATA : ConstructorsDataFile()
}

def help():
    MenuUtils.display_menu_help(app_functions)

app_functions = {
    "get" : {
        "stats" : {
            "constructor" : DummyFunction(f1_datasets),
            "driver" : DummyFunction(f1_datasets)
        }
    },
    "help" : help,
    "quit" : quit
}


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
            if next_input not in current_action.keys():
                print("Invalid Command : ", " ".join(inputs))
                MenuUtils.display_menu_help(app_functions)
                # Hit something we don't recognize, get out of this loop
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