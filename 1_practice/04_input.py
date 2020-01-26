'''
    At least in your early days of programming, you will be asking users to 
    provide you with information from the command line. In that case, you use the 
    input() function to collect that information.
'''

'''
    What is the type of user_input
'''
user_input = input("Enter your age > ")
print("1. ", type(user_input), user_input)

'''
    Will this casting work?
    Will it always work? 
    What could cause an issue?
'''
user_input = input("Enter your age > ")
user_age = int(user_input)
print("2. ", type(user_age), user_input, user_age)

'''
    Is the below code correct? If not, why and how can you fix it?
'''
user_input = input("Enter your age > ")
if user_input > 30:
    print("3. You're old!")
else:
    print("4. Do you have Snapchat?")


