'''
    Using the utilities from multi_command_utils, we can write a very basic
    application that uses a multi command application to perform tasks. 

    To do so, we have to declare a dictionary as defined in 
    
        multi_command_utils.menu_utils

    Then, we create an application to run it for us an interact with the user.

    Given the folder structure, we first must set the path to the root path
    (6_DeepProjects) so that the script will be able to find and load our 
    utilities.
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

'''
    Now we can import the application and it will load ok. 
'''
from multi_command_utils.multi_command_application import MultiCommandApp

'''
    Import the IFunction instance (in this directory) that we want to use
    from the application.
'''
from MenuIFunction.example_function import ExampleFunction

'''
    Define the functions to be hit from the program
'''
def example_one():
    print("You hit the first example")

'''
    Program Menu

    In this example we use a mix of standard Python functions (1) and IFunction
    instances (1).

    The MultiCommandApp knows how to initiate either type of functionality
    internally. 

    The bonus with using the IFunction instance is that:
        1. We are given basic functionality for free (help/argument parsing)
        2. The function instance can take somethign called a data_set. This
           can be any type of data you want to whare across IFunction instances.
        3. The IFunction instance can take additional parameters making your
           functionality much more robust.
'''

data_set = ["This", "is", "example", "data!"]

app_menu = {
    "hit" : {
        "me" : {
            "first" : example_one
        }
    },
    "try" : {
        "function" : ExampleFunction(data_set)
    }
}

'''
    Finally we create the application.

    By default if help/quit/clear are not in the menu, they will be added
    for us, so we don't even need to define it.

    Run the app (python example.py) and try the following commands
    -   help
    -   hit me first
    -   clear
    -   quit 
'''
app = MultiCommandApp("IFNTEST", app_menu)
app.run()