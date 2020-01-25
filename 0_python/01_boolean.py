'''
    A boolean value is a common construct in all programming languages. It can be one of 
    two discrete values: 
        True or False

    The words 'True' and 'False' are special words in the Python language. Other programming 
    languages similarly have special words for True and Fals as well. The underlying value of 
    a boolean is typically an integer (number) that has a value of 1 or 0. 

    In programming we call this signalled (1) or not signalled (0)

    Boolean values play a key role in any programming language. How to execute a program 
    typically comes down to checking if a value is True or False to determine what path we 
    should execute.

    This is also true in most things we do every day. For example:

    If the door is open, leave the room. 

    In this case the boolean value is (door is open). That can have one of two discrete values 
    True (door is open) or False (door is closed)

    We can also do boolean math, you should understand that as well... this section will introduce
    two more reserved words in Python : and , or

    NOTE: 
        This file will use something called casting, but to know more go to 2_casting.py
'''

'''
    Create a boolean value and print out it's type and value. 

    Notice its just another variable we set the value of one of the reserved words
    True or False to.
'''
myBooleanValue = True
print(type(myBooleanValue), myBooleanValue)

myBooleanValue = False
print(type(myBooleanValue), myBooleanValue)


'''
    We can also find out the underlying value that represents True and False
    by casting it to an integer. 

    Note that casting doesn't come up until the next file, but talking about booleans
    made sense to do before we talked about casting.
'''
print("True is = ", int(True), "False is = ", int(False))


'''
    You can perform what is called boolean math with booleans. It's also something you would 
    learn if you took a logic design (circuitry) class. 

    Again, this is useful for determining program direction. 

    There are really three operations that you would consider using. 

    and - This is called boolean multiplication. Remeber a boolean is either a 1 or a 0. 
          So when you multiply (and) two or more boolean values if the result is 1 then it's
          True and False otherwise.

    or -  This is called boolean addition. We you add (or) two or more boolean values you are 
          just taking the sum. So if it's value is 1 or greater it's True and False otherwise.

    not - This one tends to confuse new programmers. It simply is changing the value of a boolean
          to the other boolean value. So 'not True' is False and 'not False' is True.
'''
print("Boolan multiplication (and)")
print( True and False)
print( True and True)
print( False and False)

print("Boolan addition (or)")
print( True or False)
print( True or True)
print( False or False)

print("Boolan not")
print( not True )
print( not False )
