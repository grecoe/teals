import os
from enum import Enum
from engine.listOps import * 
from engine.listQuestion import *

results = {}
questionNumber = 1

# The list we are going to use in this quiz
yourListName = "aListObject"
testList = ['Sunday', 'Monday','Tuesday', "Wednesday"]


class ListOperation(Enum):
    index = 1
    extend = 2
    pop = 3
    contains = 4

def getUserResponse(listop, listoperation):
    global questionNumber
    global results
    os.system("cls")

    result = None
    listQ = listQuestion(listop)
    if listoperation == ListOperation.index:
        count = 1
        if len(listop.arguments) > 1:
            count = listop.arguments[1] - listop.arguments[0]
        result = listQ.getIndexResponse(count)
    elif listoperation == ListOperation.extend:
        result = listQ.getExtendResponse()
    elif listoperation == ListOperation.pop:
        result = listQ.getPopResponse()
    elif listoperation == ListOperation.contains:
        result = listQ.getContainsResponse()

    results[questionNumber] = result
    questionNumber += 1
    input("\nPress enter to continue..")
  
def showResults():
    os.system('cls')
    global results
    questionCount = len(results)
    correctCount = 0
    for key in results.keys():
        if results[key]:
            correctCount += 1

    percentage = (correctCount / questionCount) * 100
    print("You got a ", percentage, "%")

l1 = Lists(yourListName, testList, ListOps.contains, "Sunday")
getUserResponse(l1, ListOperation.contains)


# Get by single index
l1 = Lists(yourListName, testList, ListOps.index, 1)
getUserResponse(l1, ListOperation.index)

# Get by single index
l1 = Lists(yourListName, testList, ListOps.index, 0)
getUserResponse(l1, ListOperation.index)

# Get by single index
l1 = Lists(yourListName, testList, ListOps.index, -1)
getUserResponse(l1, ListOperation.index)

# Get by multiple index
l1 = Lists(yourListName, testList, ListOps.index, 1,3)
getUserResponse(l1, ListOperation.index)

# Append
l1 = Lists(yourListName, testList, ListOps.append, "Thursday")
getUserResponse(l1, ListOperation.extend)

# Extend
subList = ['Friday', 'Saturday']
l1 = Lists(yourListName, testList, ListOps.extend, subList)
getUserResponse(l1, ListOperation.extend)

# Generic Pop
l1 = Lists(yourListName, testList, ListOps.pop)
getUserResponse(l1, ListOperation.pop)

# Specific Pop
l1 = Lists(yourListName, testList, ListOps.pop, 1)
getUserResponse(l1, ListOperation.pop)

# Does it contain something
l1 = Lists(yourListName, testList, ListOps.contains, "Sunday")
getUserResponse(l1, ListOperation.contains)

# Does a string (which can act like a list in this case, contain something)
l1 = Lists("aSimpleString", "abcdefg", ListOps.contains, "de")
getUserResponse(l1, ListOperation.contains)


showResults()


