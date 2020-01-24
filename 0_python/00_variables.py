'''
    A variable in Python is simply some named object that contains some sort 
    of information your program needs. 

    A variable in python can hold ANY valid Python object. 

    In the example below, we use a variable called myVar and set it to various 
    values and print them. 

    But, it's important to note that the name myVar is not special, you can change
    that name to anything you want!

    NOTE: 
    
    A couple of important things to note here, I'm going to introduce some built in Python functions. 
    It's not important to know what a function is at this point, but to understand what these are:
    
    print() : Allows you to print information to the terminal. It takes either one or several items 
              to print. For example:
                print(value1 + value2) 
                    Adds value1 and value2 and prints the results. 
                print(value1, value2)
                    Prints value1 and value2 with a space between them. 
    type() : Tells you what type of object something is

    Keywords:
        parameter, print(), type()
'''

myVar = 1
print("myVar is a", type(myVar), "and the value is", myVar)
myVar = "hello"
print("myVar is a", type(myVar), "and the value is", myVar)
myVar = 1.0
print("myVar is a", type(myVar), "and the value is", myVar)


'''
    New Keyword:    IMMUTABLE. An immutable object is one that cannot be changed. For now, 
                    all we have seen are numbers and strings. These types in Python are immutable.
                    When changing the value of an immutable variable, you really are getting a 
                    different object placed within that variable. 

    Now we've seen that myVar has been used to hold an int, string and float. 

    We can create new parameters that point to an existing parameter. This can 
    be thought of as an 'alias' to the existing parameter.  
'''
myNewVar = myVar
print("Immutable alias myNewVar=", myNewVar,"myVar=", myVar)

'''
    However, if we change one of these variables, it won't change the other...why?

    These types of data are immutable. That is, a 5 is always a 5 and can't be anything else. 
'''
myVar = 7
print("Immutable alias myNewVar=", myNewVar,"myVar=", myVar)

'''
    New Keyword:    MUTABLE. A mutable object is one that CAN be changed without changing the 
                    underlying memory object. For now, I will introduce this concept using a list
                    which you won't see for a bit. However, you should come back to this file after
                    you get through 08_list or 09_dictionary, two mutable types in Python. 

    How does this work with things that are mutable (you can change them)?

    What types are mutable? Well for starters, lists and dictionaries (which you won't get to for a while)
'''
myVar = [1,2,3,4]
myNewVar = myVar
print("Mutable alias myNewVar=", myNewVar,"myVar=", myVar)

'''
    Since the value is mutable, if we change one we change the other as well....the alias is just a pointer
    to the same memory space in the computer.
'''
myNewVar[1] = "changed"
print("Mutable alias myNewVar=", myNewVar,"myVar=", myVar)

'''
    So aliasing is just providing another parameter that points to the same memory. If you changed a mutable 
    type, everything that is pointing to it will have the changes. If you point to an immutable type, only 
    the alias you modified is changed.
'''
