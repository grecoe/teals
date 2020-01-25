'''
    Comparing values is a critical part of any programming language and Python is no exception.
    Comparisons generate a boolean value (True or False). 

    You will have to compare things such as numbers or strings. You can do a lot of comparison 
    types, but think of math, with a couple of differences. 

    As we saw in variable 'var = 10', the single equal sign is used for assigning a value 
    to a variable. Here are the table of common comparisons. 

    ==  : Equal
    !=  : Not Equal
    <   : Less than
    <=  : Less than or equal
    >   : Greater than
    >=  : Greater than or equal 
    and : Both sides are true
    or  : One side is true
    not : Toggle from True to Fals or vice versa

    Using numbers an booleans these make the most sense. Of course, you can use them on strings 
    and other types, but the use there becomes much more complicated. 

'''

'''
    Do a bunch of comparisons and print out the boolean value. Can you guess what will be 
    printed before you run this program?
'''
print("1.", 1 == 5)
print("2.", 1 != 5)
print("3.", 2 < 2)
print("4.", 2 <= 2)
print("5.", 3 > 3)
print("6.", 3 >= 3)
print("7.", True and True)
print("8.", True and False)
print("9.", True or False)
print("10.", False or False)
print("11.", not True)
print("12.", not False)
# Show that True really is equal to 1
print("13.", (True and True) == 1)
# However, False is NOT equal to 0 by default
print("14.", (True and False) == 0)
# But since the underlying integer value is 0, if we cast it, it works.
print("15.", int(True and False) == 0)


