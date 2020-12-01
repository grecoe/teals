import os
import random
from utils.tracer import TraceDecorator


@TraceDecorator
def description():
    print("""
A simple program that will show you how to use a random number
generator by mimicking the toy Magic 8 Ball.

Ask questions and be amazed at the answers!
""")


@TraceDecorator
def play():
    magic8Ball = [
        "Ask again later",
        "Outlook is good",
        "Yes",
        "No",
        "Most likely no",
        "Most likely yes",
        "Maybe",
        "Outlook is not good"
    ]

    print("Ask the Magic 8 Ball anything. Enter q to quit.\n")

    question = input("What is your question? : ")
    while question != "q":
        print("You asked: ", question)
        answer = magic8Ball[random.randint(1, len(magic8Ball)) - 1]
        print("Magic 8 ball answer: ", answer)
        input("\nPress any key to play again....")
        os.system('cls')
        question = input("\nWhat is your question? : ")

    print("Thanks for playing, bye!")