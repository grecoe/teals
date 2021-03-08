import json

def dummy_func():
    print("dummy_func called")

# Show how a dict can have any sort of value
basic_dict = {
    "int": 1,
    "float": 2.0,
    "string": "Data",
    "array": [],
    "collection" : {},
    "dummy" : dummy_func
}


# Iterate those values and see what you actually have.
for key in basic_dict:

    if isinstance(basic_dict[key], int):
        print("INTEGER VALUE", key, basic_dict[key])
    elif isinstance(basic_dict[key], float):
        print("FLOAT VALUE", key, basic_dict[key])
    elif isinstance(basic_dict[key], str):
        print("STRING VALUE", key, basic_dict[key])
    elif isinstance(basic_dict[key], list):
        print("LIST VALUE", key, basic_dict[key])
    elif isinstance(basic_dict[key], dict):
        print("DICTIONARY VALUE", key, basic_dict[key])
    elif callable(basic_dict[key]):
        print("FUNCTION", key, basic_dict[key])
        # Call it!
        basic_dict[key]()
    else:
        print("NO IDEA WHAT THIS IS")

# Common usages
#   Configuraiton settings
#   Tracking data
#   Program context
#   Easily translated to JSON

"""
    When starting you'd ask for information to fill in here, but going to assume
    we've already done that.
"""
tic_tac_toe_context = {
    "board_width": 3,
    "player_count": 2,
    "available_marks": ["X","O"],
    "players": {
        "X" : {
            "name": "Dan",
            "turns": 0
        },
        "O": {
            "name": "Jody",
            "turns": 0
        },
    },
    "board" : [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
}

turn = 0
while turn < len(tic_tac_toe_context["board"]):
    current_mark = tic_tac_toe_context["available_marks"][ (turn % 2)]
    current_player = tic_tac_toe_context["players"][current_mark]["name"]
    print("It's now", current_player, "'s turn.")

    turn+=1

# Now save the context

string_context = json.dumps(tic_tac_toe_context, indent=4)
with open("./tttcontext.json", 'w') as context_file:
    context_file.writelines(string_context)