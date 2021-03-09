import json
import random

game_options = {
    "gender" : ["Male", "Female"],
    "hair_color":  ["Blond", "Brown", "White"],
    "hair_type" :  ["Curly", "Straight", "Short", "Bald"],
    "glasses": [True, False],
    "beard": [True, False],
    "moustache":  [True, False],
    "hat": [True, False]
}

# All options
player_descriptions = None
# This is a list of all the whittled down selections
selection_list = {}
# List of options already chosen
user_chosen_selections = {}

with open("guess_who.json", "r") as config:
    player_descriptions = config.readlines()
    player_descriptions = json.loads("\n".join(player_descriptions))

# This is the randomly selected person you have to guess.
possible_players = list(player_descriptions.keys())
randomly_selected_player = possible_players[random.randint(0,len(possible_players)-1)]
print(randomly_selected_player)

def show_options(options_dict, current_selections):
    print("What would you like to select on >")

    shown_options = {}
    index = 1
    for opt_key in options_dict:
        if opt_key not in current_selections:
            shown_options[index] = opt_key
            print("\t{} - {}".format(index, opt_key))
            index += 1

    selection = input("\nChoose a number between 1-{} : >".format(index-1))
    # Have faith they ONLY put in something valid....
    current_selections[shown_options[int(selection)]] = None
    return shown_options[int(selection)]


def get_option_details(option_details):

    print("Choose the details: >")
    index=1
    shown_options = {}
    for opt in option_details:
        shown_options[index]=opt
        print("\t{} - {}".format(index, opt))
        index += 1

    selection = input("\nChoose a number between 1-{} : >".format(index-1))
    # Have faith they ONLY put in something valid....
    return option_details[int(selection)-1]


def filter_options(global_player_options, selected_users, current_options):

    current_list = None
    filtered_selections = {}

    if len(selected_users) != 0:
        current_list = selected_users
    else:
        current_list = global_player_options

    for person in current_list:
        passes = True
        for opt in current_options:
            if current_list[person][opt] != current_options[opt]:
                passes = False
                break

        if passes:
            filtered_selections[person] = current_list[person]

    selected_users.clear()
    selected_users.update(filtered_selections)


while True:
    chosen_option = show_options(game_options, user_chosen_selections)
    selected_option = get_option_details(game_options[chosen_option])
    user_chosen_selections[chosen_option] = selected_option

    filter_options(player_descriptions, selection_list, user_chosen_selections)

    remaining_options = list(selection_list.keys())
    print("Currently down to {} choices - {}".format(len(selection_list), remaining_options))

    if len(remaining_options) == 0:
        print("You don't have any more choices")
        break
    elif randomly_selected_player not in remaining_options:
        print("You have no hope because the selection isn't even present....it was ",randomly_selected_player )
        break


