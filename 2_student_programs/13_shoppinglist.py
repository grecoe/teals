shopping_cart = [
    ['tooth paste', 'q-tips', 'milk'],
    ['milk', 'candy', 'apples'],
    ['planner', 'pencils', 'q-tips']
]

'''
    Helper funciton to make sure we are in bounds
'''
def validate_indexes(cart, list_no, item_no = -1):
    '''
        Assumes we are getting shopping_cart passed in, or
        a list of lists. It will validate that the indexes
        do indeed fall into the acceptable ranges for both
        list number and item number (if provided)
    '''
    return_value = False

    if list_no >= 0 and list_no < len(cart):
        if item_no != -1:
            if item_no >=0 and item_no < len(cart[list_no]):
                return_value = True
        else:
            return_value = True

    return return_value


'''
    Action functions that will do something
'''
def update_list(cart, list_no, item_no, new_item):
    if not validate_indexes(cart, list_no, item_no):
        print("Indexes out of range", list_no, item_no)
    cart[list_no][item_no] = new_item

def print_item(cart, list_no, item_no):
    if not validate_indexes(cart, list_no, item_no):
        print("Indexes out of range", list_no, item_no)
    print("   ", cart[list_no][item_no])

def print_list(cart,list_no):
    if not validate_indexes(cart, list_no):
        print("Indexes out of range", list_no)
    print("   ", cart[list_no])

'''
    Helper funcitons to keep commands siloed and not
    clutter up the application code
'''
def process_update_list(cart):
    list_no = int(input("Which list do you want to modify? > ")) -1
    item_no = int(input("Which item do you want to modify? > ")) -1
    item = input("New item? > ")

    update_list(cart,list_no, item_no, item)
    print_list(cart, list_no)

def process_print_item(cart):
    list_no = int(input("Which list do you want to print from? > ")) -1
    item_no = int(input("Which item do you want to print? > ")) -1

    print_item(cart, list_no, item_no)

def process_print_list(cart):
    list_no = int(input("Which list do you want to print? > ")) -1

    print_list(cart, list_no)




'''
    Application code
'''
commands = ['update list', 'print item', 'print list', 'quit' , "something"]

while True:
    '''
        Note that all of the actual work was done in sub functions
        so that it didn't clutter this. Maybe too complicated for 
        the kids? But sharing with you anyway. 
    '''
    command = input("What is your next action? > ")

    if command.lower().strip() == commands[0]:
        process_update_list(shopping_cart)
    elif command.lower().strip() == commands[1]:
        process_print_item(shopping_cart)
    elif command.lower().strip() == commands[2]:
        process_print_list(shopping_cart)
    elif command.lower().strip() == commands[3]:
        print("Thanks for playing...")
        break
    elif command.lower().strip() == commands[4]:
        print("Well that's something....")
    else:
        print("The command you entered is not known...valid commands are:")
        for command in commands:
            print("   ", command)


