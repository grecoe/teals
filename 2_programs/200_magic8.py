'''
    To generate a random number you can use the built in Python library random. It will
    give you random numbers so you don't need to generate them on your own. 
'''
import random


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

print("Ask the Magic 8 Ball anything. Enter q to quit.")

question = input("What is your question? : ")
while question != "q":
    print("You asked: " , question)
    answer = magic8Ball[random.randint(1, len(magic8Ball)) - 1]
    print("Magic 8 ball answer: ", answer)
    question = input("\nWhat is your question? : ")

print("Thanks for playing, bye!")