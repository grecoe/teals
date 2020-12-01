"""
TicTacToe Outline
"""

# Include the logger so we can output from here as well
import os
from utils.tracer import TraceDecorator, Logger


def log(message):
    Logger.add_log("TICTACTOE : {}".format(message))


@TraceDecorator
def description():
    print("""
Tic Tac Toe is a two player game. The game board is a grid of 9
slots and each player is assigned a mark of either X or O.

Players take turns placing a mark on the grid and will win when
they get 3 marks in:

1. A row of the grid
2. A column of the grid
3. A diagonal from corner to corner on the grid
""")


@TraceDecorator
def print_board(board, width):
    start = 0
    span = width
    while span <= len(board):
        print(" | ".join(board[start:span]))
        start = span
        span += width


@TraceDecorator
def get_winner(board, dimension, user_marks):
    # Row -> row*dimension + col
    # Col -> col*dimension + col
    # Forward -> row*dimension + row
    # Backward -> (row * 3) + (3 –row-1) -> (row * 3) + (2 –row)

    rows = []
    cols = []
    diag_forward = []
    diag_backwards = []
    for row in range(dimension):
        # Get diagonal data
        diag_forward.append(board[row * dimension + row])
        diag_backwards.append(board[(row * 3) + (2 - row)])
        # Get row column data
        rw = []
        cl = []
        for col in range(dimension):
            rw.append(board[row * dimension + col])
            cl.append(board[col * dimension + row])
        rows.append(rw)
        cols.append(cl)

    over = False
    winner = None
    setting = None

    over, winner = is_winner(rows, user_marks)
    if over:
        setting = "Row"

    if not over:
        over, winner = is_winner(cols, user_marks)
        if over:
            setting = "Column"

    if not over:
        over, winner = is_winner(diag_forward, user_marks)
        if over:
            setting = "Forward Diagonal"

    if not over:
        over, winner = is_winner(diag_backwards, user_marks)
        if over:
            setting = "Backwards Diagonal"

    return over, winner, setting


@TraceDecorator
def is_winner(collection, user_marks):
    over = False
    winner = None

    if isinstance(collection, list):
        if isinstance(collection[0], list):
            for sub_collection in collection:
                over, winner = check_collection(sub_collection, user_marks)
                if over:
                    break
        else:
            over, winner = check_collection(collection, user_marks)

    return over, winner


@TraceDecorator
def check_collection(collection, user_marks):
    single_mark = False
    winning_mark = None

    marks = list(set(collection))
    if len(marks) == 1:
        if marks[0] in user_marks:
            single_mark = True
            winning_mark = marks[0]

    return single_mark, winning_mark


# This is the Entry point to tell them about.
@TraceDecorator
def play():
    log("Start Game")

    print("\nWelcome to TicTacToe\n")

    # Program Variables
    marks = ['X', 'O']
    players = []
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    board_range = range(len(board))

    # Get user names and print out what was entered
    players.append(input("Enter name for player 1: > "))
    players.append(input("Enter name for player 2: > "))
    print("Player {} using mark {}".format(players[0], marks[0]))
    print("Player {} using mark {}".format(players[1], marks[1]))

    input("Press any key to start the game.")

    log("Players - {}".format(players))

    winner = None
    over = False
    option = None

    for turn in board_range:
        os.system('cls')

        # Each turn get current player
        current_player = turn % 2
        # The current selected position (None == not selected)
        current_position = None

        # Print out the board
        print_board(board, 3)

        # Create a prompt for the user telling them valid selections.
        prompt = "{} choose a position between {} and {} > ".format(
            players[current_player], 1, len(board)
        )

        # While user selection not made, keep going.
        while current_position is None:
            # Get the user selection
            current_position = int(input(prompt)) - 1

            if current_position not in board_range:
                # Selection is invalid index
                print("{} you have chosen an invalid position, try again".format(players[current_player]))
                current_position = None
            elif board[current_position] in marks:
                # Selected position already taken
                print("{} that position is already taken, try again.".format(players[current_player]))
                current_position = None

            log("{} chose {}".format(players[current_player], current_position))

        board[current_position] = marks[current_player]

        over, winner, option = get_winner(board, 3, marks)
        if over:
            log("Game ended : {} wins with {}".format(winner, option))
            break

    os.system('cls')
    print_board(board, 3)

    if over:
        player_name = players[marks.index(winner)]
        print("Player {} won by securing a {}".format(player_name, option))
    else:
        # If you get here, 9 turns were taken so there must be no winner?
        print("\nGame was a tie, thanks for playing\n")

    log("End Game")
