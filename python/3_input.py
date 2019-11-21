'''
   Sometimes it is neccesary to get input from a user. Python makes that pretty easy with the 
   built in function input()

   The input() function takes a single parameter and that is the string to display to the user. 
   You use that input to give them a hint of what you want them to enter. 

   NOTE: 
        input() ALWAYS returns a string value of what the user entered. If you need another type
        you will be responsible for casting it to antoher value type. See 2_casting.py for more. 

    Keywords:
        input()
'''

# Run this a couple of times with different values, it prints out teh string you entered and 
# tries to cast it to an integer in the print statment. 
myAgeString = input("So, how old are you? > ")
print("String = ", myAgeString, "Int = ", int(myAgeString))
