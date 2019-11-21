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
    
    Keywords:
        casting, int(), float(), str()
'''

stringInt = "100"
stringFloat = "1.5"

# Cast these to the type you want.
myInt = int(stringInt)
print("Int = ", myInt)

myFloat = float(stringFloat)
print("Float = ", myFloat)

# You can use casting in the print function!
print("String = ", str(myInt))
print("String = ", str(myFloat))

# But be careful, you might not get what you expect!
print(int("This is clearly not an integer!"))


