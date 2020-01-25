'''
    Casting is used in many programming languages to convert an object of one type to another. 

    Lets say we had a floating point value of 1.2. That value, we need to have no decimal point, and 
    for that matter we don't care about the precision after the floating point. 

    It would be nice to be able to cast that floating point value to an integer wouldn't it? 

    Another example is if we get some input from a user but we need a number. We can also cast
    a string to an int or a float. 

    Casting takes the form:
        <type>(<toconvert>)

        <type> = The name of the type you want to convert to int, float, str, etc.
        <toconvert> = The value to be cast to another <type>

    WARNING: 
        Trying to cast something to a type that is not supported will cause an error. 

        For example, trying to cast the string 'Essex North' to an integer doesn't make sense right?
        Well the Python language would agree and will cause an error. 
    
'''

'''
    Create two variables that hold either integer or floating point values. 

    Then we'll cast them to an actual numeric type and print out the values.

    What happens if you cast a float to an integer?
'''
stringInt = "100"
stringFloat = "1.5"

myInt = int(stringInt)
print("Int = ", myInt)

myFloat = float(stringFloat)
print("Float = ", myFloat)


'''
    Casting to string you will always be safe. Everything in Python has a string
    representation.  
'''
print("String = ", str(myInt))
print("String = ", str(myFloat))

# But be careful, you might not get what you expect! You will get an error in your program!
print(int("This is clearly not an integer!"))


