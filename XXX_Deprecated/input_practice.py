'''
    Input is one way to get information from a user for any number of reasons. 

    Python input() funciton gives a prompt to the user and collects their input,
    but the important thing to remember is it ALWAYS returns a string. So, if you need
    it in another form, you will have to cast it. 
'''

'''
    We have input thats supposed to be a number...but remember, input() only returns
    a string value. When you are brining in user input, you will have to cast (0_python\casting.py)
    the value input to some type you will want. 

    This is a little more advanced because we are also going to check that the casting worked. We 
    do this with a try/except block (4_advanced\exceptions.py) to make sure our program won't fall 
    over if given bad input. 
'''
number_input = input("Enter a number > ")
print("Current Type :", type(number_input), " = ", number_input)
try:
    actual_number = int(number_input)
    print("Current Type: ", type(actual_number) , " = ", actual_number)
except Exception as ex:
    print("Error: ", str(ex))

'''
    Because input always gives us a string, we can also instruct the user to give 
    us information separated by some character. In the example below, we ask that they 
    use a space to separate values. 

    NOTE: The example does NOT care if numbers are given or not. It will just split 
    the string entered by the user into a list by using the space character to do so.
'''
list_input = input("\nEnter several numbers separated by spaces> ")
list_numbers = list_input.split(" ")
for num in list_numbers:
    print(num)