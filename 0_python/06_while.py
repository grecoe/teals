'''
    Comparisons and boolean are important, and they will continue to be throughout all your 
    programming tasks. 

    The while loop allows you to continue to execute statements 'while' some condition is true. 

    while <expr> :
        <statements>

    <expr> here is just like in the if statement. It needs to evaluate to a boolean value and 
    can be a composition of comparisons and boolean math. 

    There will be times you want to get out of a while loop because some condition has been met. To 
    do so, of course you could set some value to make the while loop expression false. However, the
    correct way to do this is to use the 'break' statement'

    'break' will immediately exit the loop. 

    So good things to review:

        1_boolean.py
        4_comparisons.py

'''

'''
    The basic while loop just iterates until it's expression is False
'''
someNumber = 0
while someNumber < 3:
    print(someNumber, "is still less than 3.")
    # Increment someNumber each time through to eventually make the loop break.
    someNumber += 1
print(someNumber, "is now greater (or equal) to 3.")

'''
    If you want to break out of a while loop on any sort of condition, you can 
    use the reserved keyword 'break'. break makes the loop code terminate.

    In this case we have an infinite loop since True can never be False so we use
    a break to get out. 
'''
while True:
    print(someNumber)
    someNumber += 1

    if someNumber > 5:
        break
print("The if statement in the while loop kicked us out!")