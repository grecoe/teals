'''
    Some applications you write may need multi level options
    to perform the tasks you want your users to follow. 

    For instance, what if you want to list certain items:

        list cart contents
        list products -shampoo
        list locations
        etc....

    These options may or may not take additional arguments. 

    The solution in this file is only one way to resolve 
    this type of problem and is not the most complex as all
    code is contained in this single file. 

    It will support the following calls

        list cart contents
        list products -shampoo
        list locations
        get price -p produt_name
        help
        quit
'''


'''
    Define functions that will be called when the user enters in 
    the appropriate command.

    Note that each function takes in an args argument which will be
    any flags that the function would support. 
'''
def parse_additional_arguments(args):
    '''
        Helper function for any exposed functions to parse additional
        arguments that may be passed to the core function.
    '''
    arguments = {}
    current_argument = None
    argument_list = []
    for arg in args:
        arg = arg.strip()
        if len(arg) == 0 :
            continue

        if arg.startswith('-'):
            if len(argument_list) and current_argument:
                arguments[current_argument] = " ".join(argument_list)
            current_argument = arg.lower()
            arguments[arg] = None
            argument_list = []
        else:
            argument_list.append(arg)

    # Make sure we don't miss any....
    if len(argument_list) and current_argument:
        arguments[current_argument] = " ".join(argument_list)

    return arguments


def list_cart_contents(args):
    parsed_arguments = parse_additional_arguments(args)
    print("list_cart_contents args = ", parsed_arguments)

def list_products(args):
    parsed_arguments = parse_additional_arguments(args)
    print("list_products args = ", parsed_arguments)

def list_locations(args):
    parsed_arguments = parse_additional_arguments(args)
    print("list_locations args = ", parsed_arguments)

def get_price(args):
    parsed_arguments = parse_additional_arguments(args)
    print("get_price args = ", parsed_arguments)

'''
    The next two sections are
        1. Functions to print out a menu which is declared as a 
           dictionary with leaf nodes being actual functions.
        2. The menu dictionary itself.
'''

''' ### Section 1 : Display Dictionary as a menu ### '''
def display_menu_help_sub(dictionary, indent):
    '''
        This function is a recursive funciton if a dictionary
        contains a dictionary called by display_menu_help
    '''
    indent_spaces = '    ' * indent
    for sub_command in dictionary:
        print(indent_spaces + sub_command)
        if isinstance(dictionary[sub_command], dict):
            display_menu_help_sub(dictionary[sub_command], indent + 1)

def display_menu_help(menu_dictionary, args):
    '''
        This function starts the process of iterating over the 
        dictionary menu. A dictionary can only contain 
            1. Keys that identify another dictionary
            2. Keys that identify actual functions.
    '''
    print("Shopping Cart Help:")
    for command in menu_dictionary.keys():
        print(command)
        if not callable(menu_dictionary[command]):
            display_menu_help_sub(menu_dictionary[command], 1)
    print('')


'''
    ### Section 2 : Define dictioanry menu ###

    Set up your program options as a dictionary with leaf nodes
    being functions to call. 
'''
menu_options = {
    "list" : {
        "cart" : {
            "contents" : list_cart_contents
        },
        "products" : list_products,
        "locations" : list_locations
    } ,
    "get" : {
        "price" : get_price
    },
    "help" : display_menu_help,
    "quit" : quit
}

'''
    Finally, we can put a program loop in place that no matter what
    is defined above, will work as expected. 

    Note that both help and quit are special cases
        1. Help needs the menu passed along
        2. Quit should have NO arguments passed along

    Run the program and try different things
        list cart contents
        list price -p kids shampoo
        help
        quit
'''
while True:   
    user_input = input("What would you like to do : > ")
    inputs = user_input.split(' ')

    if len(inputs) > 0 and inputs[0] in menu_options.keys():
        current_action = menu_options
        last_command_index = 0
        for next_input in inputs:
            next_input = next_input.strip()
            if len(next_input) == 0 :
                continue

            last_command_index += 1
            if next_input not in current_action.keys():
                print("Invalid Command : ", " ".join(inputs))
                display_menu_help(menu_options, None)
                # Hit something we don't recognize, get out of this loop
                break
            elif callable(current_action[next_input]):
                if next_input == 'help':
                    # Special case is help where we need to pass in our menu
                    # dictionary, all others expect just the remainder of the 
                    # arguments provided.
                    current_action[next_input](menu_options, inputs[last_command_index:])
                elif next_input == 'quit':
                    # Second special case, quit will print out whatever we
                    # pass in, but we really just want to quit.
                    current_action[next_input]()
                else:
                    current_action[next_input](inputs[last_command_index:])

                # Don't iterate more, the remainder must be arguments
                break
            else:
                current_action = current_action[next_input]
    else:
        print("Invalid Command : ", " ".join(inputs))
        display_menu_help(menu_options, None)