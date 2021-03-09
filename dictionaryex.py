import json


"""
    Tic Tac Toe Review

    You know lists? Use them :)
"""

users = ["Joe", "Fred"]
marks = ["X", "O"]
board = ['', '', '', '', '', '', '', '', '']
turns = 0

while turns < 9:
    # We can simulate 2 players using modulo math, get an index and then use
    # that with users/marks
    current_index = turns % 2

    print("Player {} with mark {} it's your turn".format(
        users[current_index],
        marks[current_index]
        )
    )
    board[turns] = marks[current_index]
    print(board)
    turns += 1

print("Game hit 9 turns")

#quit()

print("\nSIMPLE DICTIONARY\n")

# Create one
simple_dict = {}

# You add to it by simply referencing a location
simple_dict["name"] = "Mr. Grecoe"
print(simple_dict["name"])

# Iterate over the dictionary using keys
for key in simple_dict.keys():
    print("Key = {}, Value = {}".format(key, simple_dict[key]))

# Remove using pop or delete
# Pop allows you to pop a key IF PRESENT or return a default value. If present
# you get the stored value.
pop_res = simple_dict.pop("foo", None)
print("POP MISSING KEY RESULT ->", pop_res)

# Delete the key MUST exist, if it doesn't you will get an exception (unlike pop)
del simple_dict["name"]
print("AFTER DELETE ->", simple_dict)

#quit()


"""
    Word counter using a dictionary.

    key = word, value = count (# of times it's been seen)

    String can be broken up using split()
"""

print("\nWORD COUNTER\n")
paragraph = """Last season, Nico Hulkenberg made a dramatic return to F1 in place of Sergio Perez and then Lance Stroll, while George Russell stepped in for Lewis Hamilton late on. As a result, Albon is staying sharp in case he's needed this season if Max Verstappen, Yuki Tsunoda, Perez or Pierre Gasly can't race for any reason."""

total_words = 0
found_words = {}
# Break up "paragraph" into seperate words.
break_down = paragraph.split(' ')
for word in break_down:
    total_words += 1

    # Strip off any periods and make lower case for checking
    cur_word = word.strip('.').lower()

    # If it's not in our dict, add it, otherwise increment count.
    if cur_word not in found_words:
        found_words[cur_word] = 1
    else:
        found_words[cur_word] += 1

# Print out some context (how many total, how many unique)
print("TOTAL WORDS:", total_words, "UNIQUE WORDS:", len(found_words))
print("ALL FOUND WORDS:\n", found_words)

# Go through and just pop each one off
for w in list(found_words.keys()):
    found_words.pop(w)

# Now our dictionary is empty
print("CLEANED DICT LEN:", len(found_words))

quit()







