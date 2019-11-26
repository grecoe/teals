'''
    Input is one way to get information from a user for any number of reasons. 

    Python input() funciton gives a prompt to the user and collects their input,
    but the important thing to remember is it ALWAYS returns a string. So, if you need
    it in another form, you will have to cast it. 
'''

# We have input thats supposed to be a number...but don't ever trust a user!
# See advanced to understand this structure. 
number_input = input("Enter a number > ")
print("Current Type :", type(number_input), " = ", number_input)
try:
    actual_number = int(number_input)
    print("Current Type: ", type(actual_number) , " = ", actual_number)
except Exception as ex:
    print("Error: ", str(ex))

# Parsing multiple inputs
list_input = input("\nEnter several numbers separated by spaces> ")
list_numbers = list_input.split(" ")
for num in list_numbers:
    print(num)