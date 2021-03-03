
def checkWinner(board, width):
    """
    Function to check winner of tic-tac-toe

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
print(checkWinner(board, 3))

# Winning board - first column
board = ["X", "2", "3", "X", "5", "6", "X", "8", "9"]
print(checkWinner(board, 3))
