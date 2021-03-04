
def checkWinnerArr(board):
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
        if len(set(board[i])) == 1:
            winner = board[i][0]

    # Check columns
    if not winner:
        for col in range(len(board[0])):
            col_data = []
            for row in range(len(board)):
                col_data.append(board[row][col])

            if len(set(col_data)) == 1:
                winner = col_data[0]

    # Check forward diagonal (easy)
    if not winner:
        diag = []
        for col_row in range(len(board[0])):
            diag.append(board[col_row][col_row])

        if len(set(diag)) == 1:
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

        if len(set(diag)) == 1:
            winner = diag[0]

    return winner


def checkWinner(board, width):
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
        if len(set(curRow)) == 1:
            winner = curRow[0]
        if len(set(curCol)) == 1:
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
        if len(set(forward)) == 1:
            winner = forward[0]
        if len(set(backward)) == 1:
            winner = backward[0]

    # returns the winners mark, if this is empty no winner.
    return winner


# Base board
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
print("Standard List - 3x3 No Winner - ", checkWinner(board, 3))

# Winning board - first column
board = ["A", "2", "3", "4", "A", "6", "7", "8", "A", "10", "11","12", "A", "14", "15","16"]
print("Standard List - 4x4 A is Winner - ", checkWinner(board, 4))


# Again but with lists
board = [
    ["1", "2", "3","A"],
    ["5", "6", "A", "8"],
    ["9", "A", "11", "12"],
    ["A", "14", "15", "16"]
]
print("List of Lists - 4x4 A is Winner - ", checkWinnerArr(board))
