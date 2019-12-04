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
print( '''
    A function is just a way to take common code and make a single copy of it.
    What is common code? Something you call more than once in your program. 
    A function is defined in your file like this :

    def [functionName](parameters if any):
        <statements>")
        [return - totally optional]
''')
pause()


print('''
    Think about Tic-Tac-Toe where you had to print the board. If you need to change the board print,
    you would only have to change it in one place if it was a function!
    
    def printBoard(board):
        print("", " | ".join(board[0:3]), "[NL] ---------[NL]", " | ".join(board[3:6]), "[NL] ---------[NL]", " | ".join(board[6:9]))
    ''')
pause()

print('''
    So, how do you return something from a function?
    Use a return statement!

    def add(x, y):
    return x + y
    ''')
pause()

print('''
    But, What if I have multiple things to return? 
    The return statment can take comma separated items and return them in that order. You
    can also put stuff in a list. 

    def doubleTheseNumbers(x, y):")
        return x*2, y*2'
    ''')
pause()

print('''
    Or use a list.... 

    def doubleTheseNumbers(x, y):
        return [x*2, y*2]
''')
pause()
