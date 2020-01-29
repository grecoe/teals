'''
    The standard python interpreter environment provides a lot of functionality
    on it's own. Objects like list and dictionary and built in functions like len() 
    and range() are at your disposal as soon as you start an interpreter. 
    
    However, there are times you will need to bring in other code to help you 
    accomplish a task. 
    
    In the standard Python distrubution there are many more modules you can import.

    This file is meant to show you how you import standard Python libraries and make
    use of them. 
  
'''

'''
    The 'os' module in Python provides access to many operating system level 
    functions. To use you simply import os
'''
import os

'''
    Now using the os path we can list all the files in the current directory.
'''
for current_dir_file in os.listdir():
    print(current_dir_file)


'''
    Another useful library in python is random. Random is a pseudo random number
    generator with even more functionality. For example, in the student programs
    you will write a War card game and will need to shuffle a deck. 

    To use the random module, just import random 
'''
import random
my_collection = ["VW", "Mercedes", "Ferrari"]
'''
    Using random, lets mix up the list above
'''
random.shuffle(my_collection)
print(my_collection)
'''
    Now let's pick a random item from the shuffled list
'''
selected_item = my_collection[random.randint(0,2)]
print("Today I'm driving my ", selected_item)