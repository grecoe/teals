'''
    The game of tic-tac-toe seems so easy, but it does take some thought in to 
    how you present it, how you get each player to make a selection, determine 
    a winner, and end the game (in a tie or otherwise)

    This program works on topics covered elsewhere in this repository

    0_Python\00_parameters.py
    0_Python\01_boolean.py
    0_Python\02_castin.py
    0_Python\03_input.py
    0_Python\04_comparisons.py
    0_Python\05_if.py
    0_Python\06_while.py
    0_Python\07_for.py
    0_Python\08_list.py
    0_Python\07_functions.py

    2_advanced\exceptions.py

    Concepts used here but not in the repo:

    set()               : https://www.geeksforgeeks.org/python-set-method/
    os.system('cls')    : https://www.geeksforgeeks.org/python-os-system-method/
    math.sqrt()         : https://www.geeksforgeeks.org/python-math-function-sqrt/
'''
import os
import math 

'''
    Global parameters to be used 
'''
turn = 0
winner = None
players = ['X','O']
board = ['1','2','3','4','5','6','7','8','9']

'''
    Print the board in one place. 
'''
def printBoard():
    global board
    print(  "", 
            " | ".join(board[0:3]), 
            "\n ---------\n", 
            " | ".join(board[3:6]), 
            "\n ---------\n", 
            " | ".join(board[6:9]))


'''
    Checking the winner requires checking 
    1. Every Row
    2. Every Column
    3. Diagonals (forward and back)
'''
def checkWinner():
    global board
    global players
    winner = None

    # Have to check rows and columns 
    width = int(math.sqrt(len(board)))
    for row in range(width):
        curRow = []
        curCol = []
        for col in range(3):
            curRow.append(board[(row*width) + col])
            curCol.append(board[(col*width) + row])

        if len(set(curRow)) == 1:
            winner = curRow[0]
        if len(set(curCol)) == 1:
            winner = curCol[0]

        if winner:
            break

    if not winner:
        forward = []
        backward = []
        for i in range(width):
            forward.append(board[i*width + i])
            backward.append(board[(i*width) + (width-i-1)])

        if len(set(forward)) == 1:
            winner = forward[0]
        if len(set(backward)) == 1:
            winner = backward[0]

    return winner

'''
    Get the next choice by the player with a few rules:

    1. Validate the user input an integer for an index
    2. Make sure the index is within the board range
    3. Make sure the chosen position is not already taken. 
'''
def getPlayerChoice(player):
    global board
    global players
    chosenIndex = None

    while chosenIndex is None:

        try:
            idx = int(input(player + " enter a space > ")) -1
        except Exception as ex:
            print("You can only enter numbers for this game")
            continue
    
        if idx not in range(len(board)):
            print("You entered an invalid number, try again.")
            continue

        # As long as the space isn't already taken, take it, otherwise try 
        # again (by continuing the loop). 
        if board[idx] in players:
            print("Space is already taken, try again...")
            continue

        chosenIndex = idx

    return chosenIndex


'''
    Run the program. 
'''

# Start by clearing the screen, welcoming the user, and printing the 
# board for the first time. 
os.system('cls')
print("Welcome to Tic Tac Toe")
printBoard()

while turn < len(board):
    # Use modulo math to toggle between players.
    player = players[turn %2]

    # Get the next selection
    playerIndex = getPlayerChoice(player)
    # Place it on the board
    board[playerIndex] = player  
    
    # Check the winner
    winner = checkWinner()
    
    # Clear the screen again
    os.system('cls')
    # Show the board
    printBoard()
    # Ibcrement the turn so we stop when needed
    turn += 1

    # If we have a winner the game is over....
    if winner :
        print(winner, " won the game")
        break

if not winner:
    print("Game was a tie!")