import random

"""
    Dictionary of possible people to guess from
"""
people = {
    'lisa': ["Female", "15","5'10", 'Red'],
    'bill': ["Male", "20", "5'5", 'Brown'],
    'linda': ["Female", "25","5'7", 'Brown'],
    'mike': ["Male", "15", "6'1", 'Blonde'],
    'liv': ["Female", "25", "5'11", 'Blonde']
}

"""
    Attributes line up with the list associated with a
    person above in the people dictionary.
"""
attributes = {
    "gender": 0,
    "age": 1,
    "height": 2,
    "hair": 3
}

"""
    Menu to choose from for the user.
"""
help_menu = {
    "list" : "prints all the charcters names",
    "gender" : "prints the gender of the chosen character",
    "age" : "prints the age of the chosen character",
    "height" : "prints the height of the chosen character",
    "hair" : "prints the hair color of the chosen character",
    "guess <name>" : "guess a character",
    "help" : "lists all the commands",
    "quit" : "quits the game"
}

"""
    Helper functions
"""


def show_dictionary(title, dictionary):
    print(title)
    for k in dictionary:
        print(k,'=', dictionary[k])


def pick_random_person(people_dict):
    keys = list(people_dict.keys())
    random_person_index = random.randint(0, len(keys) - 1)
    return keys[random_person_index]


def get_user_attribute(rand_name, user_input, attributes_dict, people_dict):
    return_value = None
    if user_input in attributes_dict.keys():
        attr_index = attributes[user_input]
        return_value = people_dict[rand_name][attr_index]
    return return_value


"""
Test out our functions
"""
randomly_selected_person = pick_random_person(people)
print("\nRandomly selected person:{}\n".format(randomly_selected_person))

hair_color = get_user_attribute(
    randomly_selected_person,
    "hair",
    attributes,
    people)

print("\n{} has {} hair\n".format)

show_dictionary("Help Menu", help_menu)
show_dictionary("People", people)

"""
    Example User Program the way it's written will loop forever,
    fix that and fill in the things you need to do.
"""
while True:

    user_input = "hair"
    # Get user input

    if user_input.lower() == "quit":
        print("End game")
        break
    elif user_input.lower() == "list":
        show_dictionary("People", people)
    elif "guess" in user_input.lower():
        print("Parse input to get name guessed and check it")
        print("Game ends regardless of result")
        break
    elif user_input.lower() in attributes.keys():
        print("Show user attribute")
    else:
        show_dictionary("Help", help_menu)
