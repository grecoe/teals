

class userInput:

    def __init__(self, options):
        numItem = 1

        self.options = {}
        for opt in options:
            self.options[numItem] = opt
            numItem += 1

    def getUserChoice(self):

        for option in self.options.keys():
            print(str(option) + '. =', self.options[option] )

        userChoice = int(input("\nWhat is your answer? : > "))

        return self.options[userChoice]