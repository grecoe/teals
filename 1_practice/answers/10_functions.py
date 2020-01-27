'''
    Once you get comfortable with functions you will use them everywhere! Becoming
    proficient with creating functions is crucial to your programming skills. 

    For this section we'll introduce a new Python module called random. This module
    creates a psuedo random number generator as well as some other useful functions. 
    The following questions will ask you to use this module:

        random.shuffle([list]) -> Randomizes the input list in place and returns nothing.
        random.randint(a,b) -> Return a number between a and b inclusive
'''
import random


'''
    1.  Write a function called myprint that takes no parameters and simply
        prints out any random string of your choosing. 

        Call the function. 
'''
def myprint():
    print("First function")

myprint()

'''
    2.  Write a function called sum that takes two parameters and returns the 
        sum (addition) of the two parameters.

        Call the function. 
'''
def sum(arg1, arg2):
    return arg1 + arg2

result = sum(5,10)
print("Second Function : ", result)

'''
    3.  Write a function called random_selection that takes a single parameter that
        is a list. The function should randomly choose a value from the list and return
        that value. 

        Call the function. 
'''
test_list = ["red", "white", "blue"]
def random_selection(input_list):
    '''
        We can use the funciton random.randint() to get possible indexs into the list. 
        We have to seed it with the outside edges of the possible list indexes.
    '''
    selection = random.randint(0, len(input_list)-1)
    return input_list[selection]

randomly_selected = random_selection(test_list)
print("Third function: ", randomly_selected)

'''
    4.  Write a function called random_shuffle that takes a single parameter that
        is an integer. 
        
        The function should create a list of numbers that has as many members in it 
        as defined by the single input parameter. 
        
        Return the shuffled list.

        Call the function. 
'''
def random_shuffle(list_count):
    '''
        We create a list to hold the values, then using the range() function 
        to provide the list of numbers to add into our return list.

        We use a for loop to add the numbers to the return list, use the random 
        library to shuffle the list, and finally return it. 
    '''
    generated_list = []
    for idx in range(list_count):
        generated_list.append(idx)
    
    random.shuffle(generated_list)
    return generated_list

shuffled_list = random_shuffle(10)
print("Fourth Function : ", shuffled_list)


'''
    5.  Write a function called multiple_return that takes no parameters.
        
        The function should return two items (whatever you want) to the caller as 
        a tuple. 
        
        Call the function and show how to use a multiple return by.
            1. Having multiple catch variables from the function
            2. Catching the return tuple and iterating those. 
'''
def multiple_return():
    return "cat", 100.45


animal, number = multiple_return()
print("Fifth Function - ", animal, number)

return_tuple = multiple_return()
for item in return_tuple:
    print("Fifth Function (tuple) - ", item)