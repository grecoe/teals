# Tic-Tac-Toe Revised

|||
|---|---|
|Goal|Create a one turn Tic-Tac-Toe game using lists, and introducting the while loop.|
|Required Reading| 0_python\00_variables.py|
||0_python\02_casting.py|
||0_python\03_comparison.py|
||0_python\04_input.py|
||0_python\05_if.py|
||0_python\06_while.py|
||0_python\08_list.py|

## Details
This program builds on the 05_TicTacToeIntroduction.md program you created.

- Allow users to keep playing (max 9 times).
- Use variables to decide whose turn it is, and greet them as Xs or Os.
- User picks a location on the board according to the number.
- Depending on the position user gave, update the corresponding position of the board to reflect that.
- Print the updated board out.
- Don't worry about tracking the winner at this point.

# Example
```
    Hello X, Enter a postion on the board > 5
    [1,2,3,4,'X',6,7,8,9]
    Hello O, Enter a postion on the board > 1
    ['O',2,3,4,'X',6,7,8,9]

    ....Continue through 9 turns....
```

# Advanced Topics

## Taking turns
Tracking who takes turns can be done with mathmatical operators.

```python
# Finding the quotient
quotient = 5//4
# Produces a 1 because 4 goes into 5 1 time
```

```python
# Finding the remainder with modulo
modulo = 5%4
# Produces a 1 because 4 goes into 5 with 1 left over
```

We can use this knowledge to figure out who goes next in a game. Particularly by using modulo.

It is common in in computer science to find out if a number is even or odd by using NUM % 2. Why?

Because if the number is even the modulo result is 0. If the number is odd the modulo result is 1. So, for a two player game with 9 turns, we can toggle between 0 and 1 for each turn, and in effect, determine if it's player 1's turn or player 2's turn.

```python
turn = 0
while turn < 9:
    print(turn % 2)
    turn += 1

"""
Result:
0
1
0
1
0
1
0
1
0
"""
```

## Printing the board
At some point you need to print out your board for a user. There are several ways to do that. Some are longer, some are shorter. Here are some examples from easiest to most efficient.

```python
board = ["1","2","3","4","5","6","7","8","9"]

# Error prone way to print board
print(board[0], "|", board[1], "|", board[2],
"\n" + board[3], "|", board[4], "|", board[5],
"\n" + board[6], "|", board[7], "|", board[8]
)

# Using list indexing makes it easier, but now you have
# to use these lines every time you want to print.
print(" | ".join(board[0:3]))
print(" | ".join(board[3:6]))
print(" | ".join(board[6:9]))

# Using a function allows you to not have to copy your print
# code everywhere!
def print_board(str_board, width):
    start = 0
    span = width
    while span <= len(str_board):
        print(" | ".join(str_board[start:span]))
        start = span
        span += width

```

## Calculate the winner
To calculate a winner you have to figure out three sets of data:
1. Rows
2. Columns
3. Diagonals

Using a list can help you with this.

Consider this algorithm
### Rows
```python
# Rows - Calcuated already above in the print_board function
```

### Columns
```python
# Rows - Calcuated already above in the print_board function
# Columns - we can use a simple formula: row*width + col, this
# will give you the index into your array.
row0_col0 = 0*3 + 0 # = 0
row1_col0 = 1*3 + 0 # = 3
row2_col0 = 2*3 + 0 # = 6
# The above would produce a[0] = 1, a[3] = 4, a[6] = 7
# Consider using two for loops to do the work of moving columns and rows
```

### Diagonals
This is considerably more complex, or is it? We can still use the formula we used for getting column data, i.e. <b>row*width + col</b>.

Given a grid (represented by a list with indexes conveniently at each position)
```
0|1|2
3|4|5
6|7|8
```
We need data at [0,4,8] and [2,4,6]

Now, if we use the formula but the same value for row and column:

```python
# Forward diagonal
# Row 0
diag1 = 0*3 + 0 # = 0
# Row 1
diag2 = 1*3 + 1 # = 4
# Row 2
diag3 = 2*3 + 2 # = 8
```

The backwards diagonal is a little more interesting at <b> row*width + (width - row - 1)</b>. Just like getting the forward diagonal, we are just going to reuse the row value. Does that work? Lets try it:
```python
# Backwards diagonal
# Row 0
diag1 = 0*3 + (3-0-1) # = 2
# Row 1
diag2 = 1*3 + (3-1-1) # = 4
# Row 2
diag3 = 2*3 + (3-2-1) # = 6
```

And that works! Now you know how to collect all of the lists that represent:
1. Rows
2. Columns
3. Diagonals

For each turn, simply collect this information and see if a player has gotten all 3 of them. If so, game over, if not, keep going!
