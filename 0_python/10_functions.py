'''
    Functions are a way to consolidate repetative or complex code.

    Main idea is to break down complex functionality to smaller problems. Smaller problems
    are then turned into functions. 

    Functions should be:
        1. Well named to understand what they are doing.
        2. Documented for users of the function
        3. Perform one set of actions  
'''

import os

def pause(message = '\nEnter to continue....', clear = True):
    if message:
        input(message)
    if clear: 
        os.system('cls')


pause()
print( '''
    A function is just a way to take common code and make a single copy of it.

    What is common code? 
    
    Something you call more than once in your program. 
    
    A function is defined in your file like this :

    def [functionName](parameters if any):
        <statements>"
        [return - totally optional]
''')
pause()

print( '''
    So a simple function that adds two numbers that you passed
    as parameters would be defined like this:

    def addTwoNumbers(number1, number2):
        return number1 + number2
''')
pause()




print('''
    Think about Tic-Tac-Toe where you had to print the board. 

    If you need to change the board print, you would only have 
    to change it in one place if it was a function!
    
    def printBoard(board):
        print("", 
            " | ".join(board[0:3]), 
            "[NL] ---------[NL]", 
            " | ".join(board[3:6]), 
            "[NL] ---------[NL]", 
            " | ".join(board[6:9]))
    ''')
pause()

print('''
    So, how do you return something from a function?

    Use a return statement! You just saw this earlier.

    def add(x, y):
        return x + y
    ''')
pause()

print('''
    But, What if I have multiple things to return? 

    The return statment can return:
    - Comma separated items (tuple) 
    - List
    - Dictionary
    - Class
    - Single item 

    def doubleTheseNumbers(x, y):
        return x*2, y*2'
    ''')
pause()

print('''
    Here is an example of using a list... 

    def doubleTheseNumbers(x, y):
        return [x*2, y*2]
''')
pause()

print('''
    Scope is important...you can access global variables 
    or use local variables. 

    global_number = 3

    def useNumbers(x):
        # We can use the global global_number variable by declaring it
        global global_number

        local_number = global_number * .5

        return x * local_number
''')
pause()

print('''
    Now, lets do a simple program that has a list of strings. 

    How could we add up all of the vowels in those strings? 

    What if we had to do it more than once in our program? 

    Lets use a function!
''')
pause()