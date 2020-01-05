
'''
    Recursion is when a function calls itself until some condition is met. 

    One of the base examples given in programming languages is the fibonacci sequence.

    That sequence looks like :

    1,1,2,3,5,8,....

    It starts with 1,1, the following numbers are the sum of the previous 
    two numbers before them. 
'''
import sys

def fib(fib_sequence, depth, first=1, second=1):
    '''
        Calculate the fibonacci sequence to some pre-caculated depth. 

        ARGUMENTS:
            fib_sequence -> List that the sequence will be stored in
            depth -> How many items in the sequence should be included
            first -> The first item for the sum
            second -> The second number for the sum

        RETURNS:
            Nothing, the sequence is kept in fib_sequence

        NOTE:
            Start by calling it leaving first and second with the defaults of 1. 
            Add a list for the collection and a depth.

            If depth is set too high, you will recieve an error:

            RecursionError: maximum recursion depth exceeded while calling a Python objec
    '''

    '''
        If the length of the sequence is 0, simply add in the first and second
        as the first items in the sequence. Otherwise append the sum of the two
        passed in arguments.
    '''
    if len(fib_sequence) == 0:
        fib_sequence.extend([first,second])
    else:
        fib_sequence.append(first + second)

    '''
        Termination of the recursion depends on reaching the desired depth, if 
        it's not there yet, it calls itself again.  
    '''
    if len(fib_sequence) <= depth:
        fib(fib_sequence, depth, fib_sequence[-2], fib_sequence[-1])


'''
    Now call it and get the first 10 entries in the sequence.
'''
sequence = []
fib(sequence, 10)
