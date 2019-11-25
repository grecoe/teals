import os
from engine.listOps import * 
from engine.listQuestion import *

results = {}
questionNumber = 1
yourListName = "aListObject"

testList = ['Sunday', 'Monday','Tuesday', "Wednesday"]

def getIndexResponse(listop):
    global questionNumber
    global results
    os.system("cls")
    count = 1
    if len(listop.arguments) > 1:
        count = listop.arguments[1] - listop.arguments[0]
    
    listQ = listQuestion(listop)
    res = listQ.getIndexResponse(count)
    results[questionNumber] = res
    questionNumber += 1
    input("\nPress enter to continue..")

def getExtendResponse(listop):
    global questionNumber
    global results
    os.system("cls")
    listQ = listQuestion(listop)
    res = listQ.getExtendResponse()
    results[questionNumber] = res
    questionNumber += 1
    input("\nPress enter to continue..")

def getPopResponse(listop):
    global questionNumber
    global results
    os.system("cls")
    listQ = listQuestion(listop)
    res = listQ.getPopResponse()
    results[questionNumber] = res
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


# Get by single index
l1 = Lists(yourListName, testList, ListOps.index, 1)
getIndexResponse(l1)

# Get by single index
l1 = Lists(yourListName, testList, ListOps.index, 0)
getIndexResponse(l1)

# Get by single index
l1 = Lists(yourListName, testList, ListOps.index, -1)
getIndexResponse(l1)

# Get by multiple index
l1 = Lists(yourListName, testList, ListOps.index, 1,3)
getIndexResponse(l1)

# Append
l1 = Lists(yourListName, testList, ListOps.append, "Thursday")
getExtendResponse(l1)

# Extend
subList = ['Friday', 'Saturday']
l1 = Lists(yourListName, testList, ListOps.extend, subList)
getExtendResponse(l1)

# Generic Pop
l1 = Lists(yourListName, testList, ListOps.pop)
getPopResponse(l1)

# Specific Pop
l1 = Lists(yourListName, testList, ListOps.pop, 1)
getPopResponse(l1)

showResults()


