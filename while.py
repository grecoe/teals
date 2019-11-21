'''

    The while loop allows you to continue to execute statements 'while' some condition is true. 

    The syntax :

    while <expr> :
        <statements>

    Just like the IF statement <expr> equates to a boolean value. 
  
'''
import os
someNumber = 0
print("h")
while True:
    print(someNumber)
    someNumber += 1
    print(someNumber)
    if someNumber > 3:
        break
