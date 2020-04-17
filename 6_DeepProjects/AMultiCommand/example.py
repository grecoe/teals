'''
    Using the utilities from multi_command_utils, we can write a very basic
    application that uses a multi command application to perform tasks. 

    To do so, we have to declare a dictionary as defined in 
    
        multi_command_utils.menu_utils

    Then, we create an application to run it for us an interact with the user.

    However, we first must set the path to the root (6_DeepProjects) so that 
    it will be able to find and load our utilities.
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
    Define the functions to be hit from the program
'''
def example_one():
    print("You hit the first example")

def example_two():
    print("You hit the second example")    

'''
    Program Menu
'''
app_menu = {
    "hit" : {
        "me" : {
            "first" : example_one,
            "second" : example_two
        }
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
app = MultiCommandApp("TEST", app_menu)
app.run()