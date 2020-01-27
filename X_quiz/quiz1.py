import os
from engine.compareOps import *
from engine.compareQuestion import *
from engine.listOps import * 

results = {}
questionNumber = 1

def promptTest(comparison):
    global results
    global questionNumber
    os.system('cls')
    cmpQuestion = compareQuestion(comparison)
    resultsanswer = cmpQuestion.getUserResponse()
    results[questionNumber] = resultsanswer
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

# Question 1 : 9 <= 9
firstcompare = Comparision(9, 9, CompareOp.lte )
promptTest(firstcompare)

# Question 2 : (9 <= 9) and True
secondCompare = Comparision(firstcompare, True, CompareOp.opand)
promptTest(secondCompare)

# Question 3 : "cat" == "Cat"
thirdCompare = Comparision("cat", "Cat", CompareOp.eq)
promptTest(thirdCompare)

# Question 4: ((9>10) and ('dog' == 'DOG')) or True
complex1 = Comparision(9, 10, CompareOp.gt)
complex2 = Comparision('dog', 'DOG', CompareOp.eq)
complex3 = Comparision(complex1, complex2, CompareOp.opand)
complex4 = Comparision(complex3, True, CompareOp.opor)
promptTest(complex4)

# Question 4: (('a' == 'b') or ('spider' == 'spider')) and ((True) and ( 8 <= 10 ))
complex1 = Comparision('a', 'b', CompareOp.eq)
complex2 = Comparision('spider', 'spider', CompareOp.eq)
complex3 = Comparision(complex1, complex2, CompareOp.opor)
complex4 = Comparision(8 , 10, CompareOp.lte)
complex5 = Comparision(True, complex4, CompareOp.opand)
complex6 = Comparision(complex3, complex5, CompareOp.opand)
promptTest(complex6)


showResults()