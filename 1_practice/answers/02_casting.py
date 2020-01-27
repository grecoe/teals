'''
    Practice with casting!

    Get a pen and paper and try and guess what the answers are before you run the program.

    The first four questions all have to do with modifying the value in the variable temperature.  
'''

'''
    What is the value of temperature?
        98.6 floating point number
    What is the type of temperature?
        temperature starts as a string type but is converted to a float type
'''
temperature = "98.6"
temperature = float(temperature)
print("1. temperature = ", temperature)
print("1. temperature type = ", type(temperature))

'''
    What is the value of temperature?
        98, the cast from float (above) to int removes the decimal and everything after it.
    What is the type of temperature?
        int
'''
temperature = int(temperature)
print("2. temperature = ", temperature)
print("2. temperature type = ", type(temperature))

'''
    What is the value of temperature?
        98
    What is the type of temperature?
        String
'''
temperature = str(temperature)
print("3. temperature = ", temperature)
print("3. temperature type = ", type(temperature))

'''
    What is the value of temperature?
        98.0
    What is the type of temperature?
        float
'''
temperature = float(temperature)
print("4. temperature = ", temperature)
print("4. temperature type = ", type(temperature))

'''
    What is the original type of measurement?
        String
    Is the following cast to float valid?  
        Why or why not?
            Yes, an integer type in string format can be formatted to a float. 
'''
measurement = "34"
measurement = float(measurement)
print("5. measurement = ", measurement)
print("5. measurement type = ", type(measurement))

'''
    We saw in the last example we could cast a string representation of an integer 
    to a float, does it work the other way?

    What is the original type of measurement?
        String
    Is the following cast to int valid?  
        Why or why not?
            No, this causes a ValueError because the string is not a pure integer.
'''
measurement = "34.2"
measurement = int(measurement)
print("6. measurement = ", measurement)
print("6. measurement type = ", type(measurement))


