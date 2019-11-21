'''
    Functions are a way to consolidate repetative or complex code.

    Main idea is to break down complex functionality to smaller problems. Smaller problems
    are then turned into functions. 

    Functions should be well named to understand what they are doing. 
'''

import os

def pause(message = '\nEnter to continue....', clear = True):
    input(message)
    if clear: 
        os.system('cls')


pause()
print("A function is just a way to take common code and make a single copy of it.")
print("What is common code? Something you call more than once in your program. ")
print("A function is defined in your file like this :\n")
print("def [functionName](parameters if any):")
print("    <statements>")
print("    [return - totally optional]")
pause()


print("Think about Tic-Tac-Toe where you had to print the board. If you need to change the board print, ")
print("you would only have to change it in one place if it was a function!\n")
print("def printBoard(board):")
print('    print("", " | ".join(board[0:3]), "[NL] ---------[NL]", " | ".join(board[3:6]), "[NL] ---------[NL]", " | ".join(board[6:9]))')
pause()

print("So, how do you return something from a function? ")
print("Use a return statement!\n")
print("def add(x, y):")
print('    return x + y')
pause()

print("But, What if I have multiple things to return?  ")
print("The return statment can take comma separated items and return them in that order. You ")
print("can also put stuff in a list. \n")
print("def doubleTheseNumbers(x, y):")
print('    return x*2, y*2')
pause()

print("Or use a list....  \n")
print("def doubleTheseNumbers(x, y):")
print('    return [x*2, y*2]')
pause()
