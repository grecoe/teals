'''
    A boolean value is a common construct in all programming languages. It can be one of two discrete 
    values : 
        True or False

    The words 'True' and 'False' are special words in the Python language. The underlying value is 
    typically an integer (number) that has a value of 1 or 0

    We can also do boolean math, you should understand that as well... this section will introduce
    two more reserved words in Python : and , or

    NOTE: 
        This file will use something called casting, but to know more go to 2_casting.py

    Keywords:
       boolean, True, False, and, or
'''

# Create a boolean value and print out it's type and value
myBooleanValue = True
print(type(myBooleanValue), myBooleanValue)

# Change the boolean value and print it out again. 
myBooleanValue = False
print(type(myBooleanValue), myBooleanValue)

# What is the underlying value of a boolean?
print("True is = ", int(True), "False is = ", int(False))

# Boolean Math

# and - This is boolean multplication. If the result is 0 the answer is False
#       otherwise you'll get a true
print("Boolan and (multiplication)")
print( True and False)
print( True and True)
print( False and False)

# or -  This is boolean addition. As long as there is ONE true in the list, the result
#       is True, otherwise it's False
print("Boolan or (addition)")
print( True or False)
print( True or True)
print( False or False)
