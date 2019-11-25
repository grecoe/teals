
from engine.userinput import *

class compareQuestion:
    
    def __init__(self, comparison):
        self.comparison = comparison

    def getUserResponse(self):

        print('What is the result of the following comparison : \n')
        print("     ", self.comparison.getStatement())
        print('\nYour options are : ')

        getChoice = userInput(['True', 'False'])
        userChoice = getChoice.getUserChoice()

        print("\nYour answer was : ", userChoice, " the answer is :", self.comparison.executeStatement())

        chosen = True
        if userChoice == "False":
            chosen = False

        return chosen == self.comparison.executeStatement()


