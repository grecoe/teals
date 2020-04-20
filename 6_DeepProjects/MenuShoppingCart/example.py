'''
    Expanding the MenuIFunction, we implement a shopping cart using all but 
    DataFile class. 

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

    Also add the import for the globals we need.  
'''
from multi_command_utils.multi_command_application import MultiCommandApp
from MenuShoppingCart.cartconstants import ShoppingCart, Categories
from MenuShoppingCart.categories import CategoriesFunction

# This instance of the cart should be passed as the dataset for the IFunction
global_cart = ShoppingCart()

'''
    All of the functionality in the menu has been stubbed with 
    this funciton. 

    Wherever you see this in the menu below, add in your own IFunction 
    class to support it. 

    The IFunction class to support categories has already been added to 
    use as a reference. 
'''
def stub():
    print("Add in functionality as an IFunction to support me")

'''
    Program Menu

    In this example, all functionality is stubbed out with the stub() 
    function that should be replaced with your own IFunction instance.
'''
app_menu = {
    "categories" : CategoriesFunction(global_cart),
    "show" : stub,
    "add" : stub,
    "remove" : stub
}

'''
    Finally we create the application.

    By default if help/quit/clear are not in the menu, they will be added
    for us, so we don't even need to define it.

    Run the app (python example.py) and try the following commands
    -   categories
        List categories that are acceptable. 
            Params: none
            Result: Show categories (dairy, meat, veg, bread, general)
    -   show
        Show the results of the cart. If no params added, print out all 
        contents. 
            Params: -c -> Category, however you want to accept it
            Result: Show cart contents either in whole or by category
    -   add
        Add an item, or list of items, to the cart. If no category is provided
        then they should end up in the 'general' category. 
            Params: -c  -> Category to add to
                    -i  -> Items, comma separated list for more than one.
    -   remove
        Remove an item, or items, from the cart regardless of what category
        it resides in. 
            Params: -i  -> Items, comma separated list for more than one.

    Default commands provided for you
    -   help
    -   clear
    -   quit 
'''
app = MultiCommandApp("CART", app_menu)
app.run()