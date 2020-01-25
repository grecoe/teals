'''
   Sometimes it is neccesary to get input from a user. Python makes that pretty easy with the 
   built in function input()

   The input() function takes a single parameter and that is the string to display to the user. 
   You use that input to give them a hint of what you want them to enter. 

   NOTE: 
        input() ALWAYS returns a string value of what the user entered. If you need another type
        you will be responsible for casting it to antoher value type. See 2_casting.py for more. 
'''

'''
    input() Always returns a string, no matter what you ask the user to input. 
'''
user_input = input("Enter your age> ")
print(type(user_input), user_input)

'''
    But, we can use casting like we did in 02_casting
'''
user_input = input("Enter your age> ")
print(type(user(input)), user_input, "Int Value = ", int(myAgeString))
