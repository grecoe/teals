'''
    This is a simple program that lets a user know if they can be president.
    The rules are:

    1. Must be over 35 years old
    2. Must have lived in the US for 14 years
    3. Must be a citizen

    This shows how to get input from the user and cast it to the types we want
    then compare the input with the rules to make a determination.

    This program works on topics covered elsewhere in this repository

    0_Python\00_parameters.py
    0_Python\01_boolean.py
    0_Python\02_casting.py
    0_Python\03_input.py
    0_Python\04_comparisons.py
    0_Python\05_if.py
'''

rule1Age = 35
rule2ResidencyYears = 14
rule3Resident = 'y'

userAge = int(input("What is your age in years? >"))
userResidencyYears = int(input("How long have you lived in the US? >"))
userCitizen = input("Are you a US citizen (y/n)? >").lower()

if userAge < rule1Age:
    print("You are not old enough to be president")
elif userResidencyYears < rule2ResidencyYears:
    print("You have not been a resident of the US long enough to be president")
elif userCitizen != rule3Resident:
    print("You must be a US citizen to be president.")
else:
    print("You can be president!")
