
import json
import random


"""
    Because we don't want to have to generate game people every time, we keep
    it in a file and then load it up.
"""
player_descriptions = None
with open("guess_who.json", "r") as config:
    player_descriptions = config.readlines()
    player_descriptions = json.loads("\n".join(player_descriptions))

"""
    If you look at the file, it's already laid out as a dictionary. Loading it with the json
    library then puts it in a true Python dictionary. We can go through the names
"""
print("PLAYER OPTIONS:")
for name in player_descriptions:
    print(name)

"""
    All players are identical in format, so we can take ANY player and then print out the
    sub dictionary of settings.

    These are the things people will be searching for.
"""
print("\nPLAYER PROPERTIES:")
for name in player_descriptions:
    for prop in player_descriptions[name]:
        print(prop)
    # We printed properties out for one user, get out.
    break

"""
    Now be more specific, show all settings for one user.
"""
print("\nSPECIFIC PLAYER PROPERTIES:")
for name in player_descriptions:
    print("Name:", name)
    for prop in player_descriptions[name]:
        print(prop, "=", player_descriptions[name][prop])
    # We printed properties out for one user, get out.
    break

"""
    The rest of this becomes a bit more complicated and not sure its appropriate for a first
    time application (but I overthink a lot)

    - Collect all names
    - For each property, collect all possible options so we can show a user
        i.e. hair color collecion, etc
    - Choose a default player we are trying to guess
    - Allow the user to choose a property, then one option from the collection for that
      property (shown as a list maybe?)
    - Filter down user list based on choice, but have to remember the previous choices
      so we really are doing a multi-layer filter to get a user.
    - End game (either they can't possibly find them because of choices or they win.)

    EVERYTHING BELOW THIS POINT IS TOO ADVANCED FOR THE BEGINNER STUDENT
"""

# All of the names of options from the file
loaded_names = list(player_descriptions.keys())
# Choose a random name from the entire list for user to guess.
guess_player_name = loaded_names[random.randint(0, len(loaded_names) - 1)]
guess_player_info = player_descriptions[guess_player_name]
# Load up all property values and keep list of what we can suggest
possible_options = {}
# The filtered list of options based on selections
filtered_on_guess = player_descriptions

# Only allow options for things that come from the file
for name in player_descriptions:
    for prop in player_descriptions[name]:
        if prop not in possible_options:
            possible_options[prop] = []

        value = player_descriptions[name][prop]
        if value not in possible_options[prop]:
            possible_options[prop].append(value)


while True:

    # Give them options they haven't already chosen
    selection_index = 1
    print("Search on what? >")
    for option in possible_options:
        print("\t{} - {}".format(selection_index, option))
        selection_index += 1

    user_choice = int(input("Which options? > "))
    user_selected_option = (list(possible_options.keys()))[user_choice - 1]

    # Now that we have that opiton, what are the choices
    selection_index = 1
    print("Choose a value for {} > ".format(user_selected_option))
    for option in possible_options[user_selected_option]:
        print("\t{} - {}".format(selection_index, option))
        selection_index += 1

    user_choice_value = int(input("Which options? > "))
    user_selected_option_value = possible_options[user_selected_option][user_choice_value - 1]

    # Now
    # 1. If the guess person has this property, remove others that dont/
    # 2. If the guess person does NOT have this property, remove those that do

    # Get the keys for names
    remaining_names = list(filtered_on_guess.keys())
    guess_player_has_value = guess_player_info[user_selected_option] == user_selected_option_value
    print("Guess player has {} {} == {}".format(
        user_selected_option_value,
        user_selected_option,
        guess_player_has_value
    ))

    # If guess_player_has_value keep everthing that matches, otherwise remove them if they have it
    for name in remaining_names:
        should_remove = False

        if guess_player_has_value and (filtered_on_guess[name][user_selected_option] != user_selected_option_value):
            should_remove = True
        elif (not guess_player_has_value) and (filtered_on_guess[name][user_selected_option] == user_selected_option_value):
            should_remove = True

        if should_remove:
            print("Removing", name)
            del filtered_on_guess[name]

    # Get them one more time
    remaining_names = list(filtered_on_guess.keys())
    if guess_player_name not in remaining_names:
        print("You can't possibly find the answer > {}".format(guess_player_name))
        break
    elif len(remaining_names) == 1:
        print("You win, you got {}".format(guess_player_name))
        break

    print("Still in the hunt > ", remaining_names)
