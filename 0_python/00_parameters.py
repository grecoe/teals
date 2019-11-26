'''
    A parameter in Python is simply some named object that contains some sort 
    of information your program needs. 

    A parameter in python can hold ANY valid Python object. 

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
