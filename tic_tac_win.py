
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


# Generate random sized list based on width
loc = 0
width = 20
large_list = [x for x in (' ' * (width * width))]
while loc < len(large_list):
    large_list[loc] = 'Z'
    loc += width

#print(large_list)
#print("Basic list representing board of {}x{} :  Z  winner - {}".format(width, width, checkWinner(large_list, width)))




# Now make a XxX board but set diagonal to R based on width
print("List of lists")
board = []
for i in range(width):
    chartouse = ' ' if i != 4 else 'A'
    board.append([x for x in (chartouse * width)])
    board[-1][i] = 'R' if chartouse != 'A' else chartouse
    print(board[-1])
print("List of Lists - {}x{} A is Winner - {}".format(width, width, checkWinnerArr(board)))
