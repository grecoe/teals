# Include the logger so we can output from here as well
from utils.tracer import TraceDecorator


@TraceDecorator
def show_description():
    print("""
Based on your choices, the program will help you pick a college
that most suits you.

Code is located at: /games/collegechooser.py

""")


@TraceDecorator
def play():
    '''
        This program uses lists and dictionaries to ask a user a preference on
        college choices then ranks the school based on those selections.
    '''

    questions = {
        "What location do you prefer? > ": ["New England", "West Coast", "New York", "South"],
        "What size school do you prefer? > ": ["Small", "Middle", "Large", "HUGE"],
        "What size city do you prefer to live in? > ": ["Small City", "Suburbs", "Big City", "Rural"]
    }

    schools = {
        "Brown":
            [0, 1, 3],
        "Panoma":
            [1, 1, 3],
        "NYU":
            [2, 3, 2],
        "Alabama State":
            [3, 1, 3]
    }

    # Key is question, value is answer
    answers = {}
    # Key is school name, value is ranking
    rankings = {}

    # Collect users input
    for question in questions:
        optionsList = questions[question]
        for idx in range(len(optionsList)):
            print(idx + 1, " ", optionsList[idx])
        answers[question] = int(input(question)) - 1

    # Rank the schools
    for school in schools:
        schoolRank = 0
        optionsIndex = 0
        schoolOptions = schools[school]
        for answer in answers:
            # This only works because we know the two lists are aligned....
            if schoolOptions[optionsIndex] == answers[answer]:
                schoolRank += 1
            optionsIndex += 1

        rankings[school] = schoolRank

    print("\nYour Rankings")
    for rank in rankings:
        print(rank, " : ", rankings[rank])
