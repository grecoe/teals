'''
    Practice with casting!

    Get a pen and paper and try and guess what the answers are before you run the program.

    The first four questions all have to do with modifying the value in the variable temperature.  
'''

'''
    What is the value of temperature?
    What is the type of temperature?
'''
temperature = "98.6"
temperature = float(temperature)
print("1. temperature = ", temperature)
print("1. temperature type = ", type(temperature))

'''
    What is the value of temperature?
    What is the type of temperature?
'''
temperature = int(temperature)
print("2. temperature = ", temperature)
print("2. temperature type = ", type(temperature))

'''
    What is the value of temperature?
    What is the type of temperature?
'''
temperature = str(temperature)
print("3. temperature = ", temperature)
print("3. temperature type = ", type(temperature))

'''
    What is the value of temperature?
    What is the type of temperature?
'''
temperature = float(temperature)
print("4. temperature = ", temperature)
print("4. temperature type = ", type(temperature))

'''
    What is the original type of measurement?
    Is the following cast to int valid?  
        Why or why not?
'''
measurement = "34"
measurement = float(measurement)
print("5. measurement = ", measurement)
print("5. measurement type = ", type(measurement))

'''
    We saw in the last example we could cast a string representation of an integer 
    to a float, does it work the other way?

    What is the original type of measurement?
    Is the following cast to int valid?  
        Why or why not?
'''
measurement = "34.2"
measurement = int(measurement)
print("6. measurement = ", measurement)
print("6. measurement type = ", type(measurement))


