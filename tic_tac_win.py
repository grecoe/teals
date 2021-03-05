"""
This file contins several options for solving the winner in tic tac toe problem.

If your program uses a single list to represent the board OR a list of lists there is a solution

    single list:    checkWinner
                    advanced_checkWinner

    list of list:   checkWinnerArr
                    advanced_checkWinnerArr

At the bottom of the file there are two functions to generate random boards with a column, row
or diagonal prefilled to test out the solvers.

Once comfortable with it, bring it into your program!
"""
import math
import random


def check_collection(collection, size, default_value):
    """
    No matter what check you are doing - straight list board, list of list board you have to check
    collections for a winner. Break that out to do the validation and it can be used in both.

    Params:
        collection - List to check
        size - Expected size of the collection
        default_value - Value to ignore in collection check.

    Returns:
        True if the collection has a set size of 1 and is NOT default value.
    """
    if len(collection) == size and len(set(collection)) == 1 and collection[0] != default_value:
        return True
    return False


def advanced_checkWinner(board, default_value=''):

    width = (int)(math.sqrt(len(board)))

    if((width * width) != len(board)):
        raise Exception("Invalid board")

    winner = None

    # Have to check rows and columns but collect the diagonals as well
    forward_diag = []
    backward_diag = []
    for row in range(width):
        # Collect diagonals
        forward_diag.append(board[row * width + row])
        backward_diag.append(board[(row * width) + (width - row - 1)])

        # A place to collect rows and columns
        curRow = []
        curCol = []

        # Get next row/column
        for col in range(width):
            curRow.append(board[(row * width) + col])
            curCol.append(board[(col * width) + row])

        # Check for a winner in this row/column pairing
        if check_collection(curRow, width, default_value):
            winner = curRow[0]
        if check_collection(curCol, width, default_value):
            winner = curCol[0]

        if winner:
            # If we have a winner just get out so we dont keep iterating the board
            break

    if not winner:
        if check_collection(forward_diag, width, default_value):
            winner = forward_diag[0]
        if check_collection(backward_diag, width, default_value):
            winner = backward_diag[0]

    return winner


def advanced_checkWinnerArr(board, default_value=' '):

    # Verify board
    for row in board:
        if len(row) != len(board):
            raise Exception("Invalid board")

    width = len(board)
    winner = None

    # Each iteration here checks a row (easy) and a column (harder)
    for row in range(width):
        if check_collection(board[row], width, default_value):
            # Check each row as you go, if we have a hit it will save us time.
            winner = board[row][0]
        else:
            # Get next column row now becomes the column idx
            col_data = []
            for act_row in range(width):
                col_data.append(board[act_row][row])

            if check_collection(col_data, width, default_value):
                winner = col_data[0]

        if winner:
            break

    # Check forward diagonal (easy)
    if not winner:
        forward_diag = []
        backward_diag = []

        # Forward is easy, backwards slightly harder
        back_row_idx = width - 1
        for base_idx in range(len(board[0])):
            forward_diag.append(board[base_idx][base_idx])
            backward_diag.append(board[back_row_idx][base_idx])
            back_row_idx -= 1

        if check_collection(forward_diag, width, default_value):
            winner = forward_diag[0]
        if check_collection(backward_diag, width, default_value):
            winner = backward_diag[0]

    return winner


def checkWinnerArr(board, default_value=' '):
    """
    Function to check winner of tic-tac-toe IF your board is an list
    of lists, i.e. [] [],[],...]

    We are NOT going to validate that this is a square, we are trusting
    the user input. The ONLY limitation is that
        # rows == #columns

    - Checks all rows
    - Checks all columns
    - Checks forward diagonal
    - Checks backwards diagonal

    If there is a winner, returns the winning mark.
    """
    winner = None

    # Check rows - for every row check to see if they are the same
    for i in range(len(board[0])):
        if len(set(board[i])) == 1 and board[i][0] != default_value:
            winner = board[i][0]

    # Check columns
    if not winner:
        for col in range(len(board[0])):
            col_data = []
            for row in range(len(board)):
                col_data.append(board[row][col])

            if len(set(col_data)) == 1 and col_data[0] != default_value:
                winner = col_data[0]

    # Check forward diagonal (easy)
    if not winner:
        diag = []
        for col_row in range(len(board[0])):
            diag.append(board[col_row][col_row])

        if len(set(diag)) == 1 and diag[0] != default_value:
            winner = diag[0]

    # Check backwards diag
    if not winner:
        start_row = len(board[0]) - 1
        start_col = 0
        diag = []
        while start_row >= 0 and start_col < len(board[0]):
            diag.append(board[start_row][start_col])
            start_row -= 1
            start_col += 1

        if len(set(diag)) == 1 and diag[0] != default_value:
            winner = diag[0]

    return winner


def checkWinner(board, width, default_value=' '):
    """
    Function to check winner of tic-tac-toe IF your board is a single array
    that represents all the slots, i.e. [....]

    We are NOT going to validate that this is a square, we are trusting
    the user input. The only limitation is that the width * width == len(board)

    - Checks all rows
    - Checks all columns
    - Checks forward diagonal
    - Checks backwards diagonal

    If there is a winner, returns the winning mark.
    """
    winner = None

    # Have to check rows and columns
    for row in range(width):
        # A place to collect rows and columns
        curRow = []
        curCol = []

        # Formula is width*row + col -> row collection
        #            width*col + row -> column collection
        for col in range(width):
            curRow.append(board[(row * width) + col])
            curCol.append(board[(col * width) + row])

        # Set function returns a collection of unique items
        # in an enumerable type (list in this case). If the count
        # is 1 then we have a winner. Save the winners mark.
        if len(set(curRow)) == 1 and curRow[0] != default_value:
            winner = curRow[0]
        if len(set(curCol)) == 1 and curCol[0] != default_value:
            winner = curCol[0]

        if winner:
            break

    # Now check the diagonals if a row/column didnt do it.
    if not winner:
        # Collections for forward/backward diagonal
        forward = []
        backward = []

        # Collect them, formulas:
        #   Forward = row * width + row
        # Backwards = (row * width) + (width - row - 1)
        for row in range(width):
            forward.append(board[row * width + row])
            backward.append(board[(row * width) + (width - row - 1)])

        # Again use set() to figure out if we have a winner.
        if len(set(forward)) == 1 and forward[0] != default_value:
            winner = forward[0]
        if len(set(backward)) == 1 and backward[0] != default_value:
            winner = backward[0]

    # returns the winners mark, if this is empty no winner.
    return winner


def build_single_list(width, default_val, set_random_row=False, set_random_col=False, set_diag=False):
    loc = 0
    single_list = [x for x in (default_val * (width * width))]

    rand_selection = random.randint(0, width-1)
    if set_random_row:
        loc = (rand_selection * width)
        for idx in range(loc, (loc + width)):
            single_list[idx] = 'R'
    elif set_random_col:
        loc = rand_selection
        while loc < len(single_list):
            single_list[loc] = 'C'
            loc += width
    elif set_diag:
        loc = 0
        while loc < len(single_list):
            single_list[loc] = 'D'
            loc += width + 1

    print(single_list)
    return single_list


def build_list_of_list(width, default_val, set_random_row=False, set_random_col=False, set_diag=False):
    loc = 0
    board = []

    rand_selection = random.randint(0, width-1)
    if set_random_row:
        for i in range(width):
            chartouse = default_val if i != rand_selection else 'R'
            board.append([x for x in (chartouse * width)])
    elif set_random_col:
        for i in range(width):
            board.append([x for x in (default_val * width)])
            board[-1][rand_selection] = 'C'
    elif set_diag:
        for i in range(width):
            board.append([x for x in (default_val * width)])
            board[-1][i] = 'D'

    for row in board:
        print(row)
    return board


# Test it all out
total_width = 5

print("Test single list - width", total_width)
lst = build_single_list(total_width, ' ', True, False, False)
print("List row winner : ", advanced_checkWinner(lst, ' '))
lst = build_single_list(total_width, ' ', False, True, False)
print("List column winner : ", advanced_checkWinner(lst, ' '))
lst = build_single_list(total_width, ' ', False, False, True)
print("List diagonal winner : ", advanced_checkWinner(lst, ' '))

print("\nTest list of lists - width", total_width)
bd = build_list_of_list(total_width, ' ', True, False, False)
print("List row winner : ", advanced_checkWinnerArr(bd, ' '))
bd = build_list_of_list(total_width, ' ', False, True, False)
print("List column winner : ", advanced_checkWinnerArr(bd, ' '))
bd = build_list_of_list(total_width, ' ', False, False, True)
print("List diagonal winner : ", advanced_checkWinnerArr(bd, ' '))

