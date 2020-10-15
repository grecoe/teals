"""
    Madlibs project
"""

introduction = """
A Day in NYC: a Mad Lib.

Welcome! You are about to play a fantastic word game.
I will ask you for nouns, verbs, adjectives, proper nouns and adverbs.
Using those words I will create an unexpected story for you!
"""

story = """
It was a {adjective2} day in {city}.

Our hero {celeb} was on a walk from the {place1} to {place2}.

{celeb} was walking rather {adverb1} because he/she had lived in {city}
for a few months.

All of a sudden a {adjective1} {noun} appeared out of nowhere!!! {celeb}
decided to {verb} {adverb2} instead of dealing with the situation.Thrown
off from {place2} {celeb} decides to go to {place3} instead.

What a {adjective2} day in {city}.
"""


# Program execution!
# 1. Show the introduction
# 2. Get user input
# 3. Show the story

# 1. The introduction
print(introduction)

# 2. Get user input
print("Now enter in some information for our story:")
user_city = input("Enter a city: ")
user_celeb = input("Enter name of celebrity: ")
user_place1 = input("Enter a place: ")
user_place2 = input("Enter another place: ")
user_adverb1 = input("Enter an adverb: ")
user_adjective1 = input("Enter an adjective: ")
user_noun = input("Enter a noun: ")
user_verb = input("Enter a verb: ")
user_place3 = input("Enter another place: ")
user_adverb2 = input("Enter an adverb: ")
user_adjective2 = input("Enter an adjective: ")


# 3. Show the story
print("\n\nYour MadLib is ready!")
print(story.format(
    city=user_city,
    celeb=user_celeb,
    place1=user_place1,
    place2=user_place2,
    adverb1=user_adverb1,
    adjective1=user_adjective1,
    noun=user_noun,
    verb=user_verb,
    adverb2=user_adverb2,
    adjective2=user_adjective2,
    place3=user_place3
))