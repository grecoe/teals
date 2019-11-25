from engine.userinput import *
from engine.listOps import *

class listQuestion:
    
    def __init__(self, listop):
        self.listop = listop

    def getIndexResponse(self, count):
        returnValue = False
        print('If the list currently is : ', self.listop.list, "\n")
        print("     ", self.listop.getStatement())
        
        if count == 1:
            print('\nWhat will you get back? : ')
            getChoice = userInput(self.listop.list)
            userChoice = getChoice.getUserChoice()
            
            executedValue = self.listop.executeStatement()
            userSelectedValue = self.listop.list[self.listop.list.index(userChoice)]

            print("\nThe result would be ", executedValue, "you said", userSelectedValue)
            returnValue = executedValue == userSelectedValue
        else:
            print('\nHow many items would you get back? : ')
            getChoice = userInput([count - 1, count + 3, count])
            userChoice = getChoice.getUserChoice()

            executedValue = self.listop.executeStatement()

            print("\nThe result would be : ", executedValue)
            print("\nThat has", len(executedValue), "values and you said ", userChoice)
            returnValue = len(executedValue) == int(userChoice)

        return returnValue

    def getExtendResponse(self):
        returnValue = False
        print('If the list currently is : ', self.listop.list, "\n")
        print("     ", self.listop.getStatement())

        print('\nHow many items will be in the list? : ')

        short = int(len(self.listop.list)/2) + 1
        long = len(self.listop.list) + short + 1
        rng = range(short, long, 1 )        
        getChoice = userInput(rng)
        userChoice = getChoice.getUserChoice()
            
        executedValue = self.listop.executeStatement()
        userSelectedValue = int(userChoice)

        print("\nThe result would be ", len(executedValue), "you said", userSelectedValue)
        return len(executedValue) == userSelectedValue

    def getPopResponse(self):
        returnValue = False
        print('If the list currently is : ', self.listop.list, "\n")
        print("     ", self.listop.getStatement())

        print('\nWhat does it return?: ')

        getChoice = userInput(self.listop.list)
        userChoice = getChoice.getUserChoice()
            
        executedValue = self.listop.executeStatement()
        userSelectedValue = userChoice

        print("\nThe result would be ", executedValue , "you said", userSelectedValue)
        return executedValue == userSelectedValue