# Include the logger so we can output from here as well
from utils.tracer import TraceDecorator, Logger


@TraceDecorator
def show_description():
    print("""
Multi dimentional arrays (we've seen these before) representing a shopping cart.

At the main menu, type in 'help' to see all options or 'q' to quit.

Code is located at: /games/cart.py
""")


@TraceDecorator
def update_list(shopping_cart):
    # The program asks which shopping list the user wants to update,
    # which position it should update, and the new value to update.

    # Takes in an integer representing the index of the shopping list,
    # an integer representing the index of the item to update, and a string
    # representing the new value for that item. Does not alter the length of the list
    list_id = int(input("Enter a list (1-{}) > ".format(len(shopping_cart)))) - 1
    item_id = int(input("Enter item (1-{}) > ".format(len(shopping_cart[list_id])))) - 1
    new_item = input("Enter new item at this position> ")

    Logger.add_log("Update list-{} item-{} value-{}".format(list_id, item_id, new_item))
    shopping_cart[list_id][item_id] = new_item


@TraceDecorator
def print_item(shopping_cart):
    # The program asks which shopping list the item is on and which
    # position it occupies, then prints the items name.

    # Takes an int representing the index of the shopping list followed
    # by an int representing the index of the item to print.
    list_id = int(input("Enter a list (1-{}) > ".format(len(shopping_cart)))) - 1
    item_id = int(input("Enter item (1-{}) > ".format(len(shopping_cart[list_id])))) - 1

    Logger.add_log("View item list-{} item-{} value-{}".format(list_id, item_id, shopping_cart[list_id][item_id]))

    print("Item at [{}][{}] = {}".format(list_id, item_id, shopping_cart[list_id][item_id]))


@TraceDecorator
def print_list(shopping_cart):
    # The program asks which shopping list the user wants and prints
    # all of the items associated with that shopping list.

    # Takes an int representing the index of the shopping list to print.
    list_id = int(input("Enter a list (1-{}) > ".format(len(shopping_cart)))) - 1
    Logger.add_log("View list-{} value-{}".format(list_id, shopping_cart[list_id]))
    print(shopping_cart[list_id])


@TraceDecorator
def print_cart(shopping_cart):
    # The program asks which shopping list the user wants and prints
    # all of the items associated with that shopping list.

    # Takes an int representing the index of the shopping list to print.
    for list_idx in range(len(shopping_cart)):
        ouptut_data = "List - {} : ".format(list_idx + 1)
        for item_idx in range(len(shopping_cart[list_idx])):
            ouptut_data += " [{}] - {}".format(item_idx + 1, shopping_cart[list_idx][item_idx])
        print(ouptut_data)


@TraceDecorator
def count_qtips(shopping_cart):
    """
    Count q-tip instances
    """
    instances = 0
    for list_idx in range(len(shopping_cart)):
        instances += shopping_cart[list_idx].count('q-tips')

    print("There are {} instances of 'q-tip' in your list!".format(instances))


@TraceDecorator
def drink_more_milk(shopping_cart):
    """
    Count q-tip instances
    """
    for list_idx in range(len(shopping_cart)):
        if 'milk' not in shopping_cart[list_idx]:
            shopping_cart[list_idx].append('milk')

    print("Finished adding milk to each list")


@TraceDecorator
def if_you_give_a_moose_a_cookie(shopping_cart):
    for list_idx in range(len(shopping_cart)):
        if 'milk' in shopping_cart[list_idx]:
            milk_index = shopping_cart[list_idx].index('milk')
            shopping_cart[list_idx][milk_index] = "milk and cookies"

    print("Updated milk entries..")


@TraceDecorator
def play():
    shopping_cart = [
        ['tooth paste', 'q-tips', 'milk'],
        ['milk', 'candy', 'apples'],
        ['planner', 'pencils', 'q-tips']
    ]

    # List of lists (like cart), first is command, second is the function to call.
    allowed_commands = [
        ["help", None],
        ["update", update_list],
        ["view item", print_item],
        ["view list", print_list],
        ["view cart", print_cart],
        ["qtip", count_qtips],
        ["milk", drink_more_milk],
        ["moose", if_you_give_a_moose_a_cookie]
    ]

    user_commands = input("What do you want to do? ").lower()
    while user_commands != 'q':

        found_command = False
        for cmd in allowed_commands:
            if cmd[0] == user_commands:
                found_command = True
                if cmd[0] == 'help':
                    # Looking for help so show them all the commands
                    for show_cmd in allowed_commands:
                        print(show_cmd[0])
                else:
                    # A valid command AND not help, call the funciton [1]
                    cmd[1](shopping_cart)
                    break

        if not found_command:
            # Unknown command, help out the user by forcing help print out
            print("The command -{}- was not found.".format(user_commands))
            user_commands = 'help'
            continue

        user_commands = input("What do you want to do? ").lower()
