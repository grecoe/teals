'''
    At least in your early days of programming, you will be asking users to 
    provide you with information from the command line. In that case, you use the 
    input() function to collect that information.
'''

'''
    What is the type of user_input?

        String, input() ALWAYS returns a string from whatever you input.
'''
user_input = input("Enter your age > ")
print("1. ", type(user_input), user_input)

'''
    Will this casting work?
        Maybe, if the user actually enters in an integer number, then yes. 

    Will it always work? 
        No, if a user types in characters or a floating point number then the cast will fail.

    What could cause an issue?
        Invalid type being entered on the command line.
'''
user_input = input("Enter your age > ")
user_age = int(user_input)
print("2. ", type(user_age), user_input, user_age)

'''
    Is the below code correct? If not, why and how can you fix it?

        No, this is not correct. input() always returns a string but the if statement is trying
        to compare that string to the integer 30. Strings and integers cannot be compared like this
        so the user_input variable first has to be casted to a int()
'''
user_input = input("Enter your age > ")
if user_input > 30:
    print("3. You're old!")
else:
    print("4. Do you have Snapchat?")


