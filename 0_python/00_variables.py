'''
    A variable in Python is simply a name given to some sort of object. That object could be a 
    number, string, or any valid python object. 
    
    You can thing of it as an alias to the actual data. For example

    num = 5

    The variable is num and it's value is 5. 

    Why do we need variables? Because programs of all kinds need to preserve data of various 
    types for futher processing. 

    The rest of this file can be executed in a Python interpreter, as all of the files ending 
    with the .py extension. But do read through it for content. 

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

    ADVANCED TOPIC:
    This is very early days to discuss what an immutable and mutable object are, but it is important
    that some of this is explained early. When you move through the content you may want to come back
    and re-read some of this content.

        IMMUTABLE.  An immutable object is one that cannot be changed. Types such as int, float, 
                    and string are immutable.
                    When changing the value of an immutable variable, you really are pointing to
                    another memory location with the new value.  

         MUTABLE.   A mutable object is one that CAN be changed without changing the 
                    underlying memory object. For now, I will introduce this concept using a list
                    which you won't see for a bit. However, you should come back to this file after
                    you get through 08_list or 09_dictionary, two mutable types in Python. 
'''

'''
    We create a variable in Python simply by making some name for it 
    and assigning a value to it. 

    Below, we create the 'myVar' variable and assing different values to
    it and then print out what type of data the variable is pointing to as
    well as the actual value held by the variable. 
'''
myVar = 1
print("myVar is a", type(myVar), "and the value is", myVar)
myVar = "hello"
print("myVar is a", type(myVar), "and the value is", myVar)
myVar = 1.0
print("myVar is a", type(myVar), "and the value is", myVar)


'''
    Now we've seen that myVar has been used to hold an int, string and float. 

    We can create new variable and set it equal to an existing variable. 
    They both point to the same memory location that holds the value. 
    
    Remember, a variable is simply an alias to some actual object.
'''
myNewVar = myVar
print("Variables (same): myNewVar=", myNewVar,"myVar=", myVar)

'''
    However, if we change one of these variables, it won't change the other...why?

    These types of data are immutable. That is, a 5 is always a 5 and can't be anything else. 
    When we change one, another object is created for us (in the case below, that is 7) and 
    now the two variables have different values. 
'''
myVar = 7
print("Variables(different): myNewVar=", myNewVar,"myVar=", myVar)

'''
    How does this work with things that are mutable (objects you can modify without creating 
    a new object in the system)?

    What types are mutable? For this example we will use a Python list. A list is a sequence of
    items and you can read more about them in 08_list.py.
    
    In this example we change the type of myVar to a list of integers and set myNewVar to 
    myVar. 
'''
myVar = [1,2,3,4]
myNewVar = myVar
print("Variables (mutable): myNewVar=", myNewVar,"myVar=", myVar)

'''
    Since the value is mutable, if we change one we change the other as well....the alias is just 
    a pointer to the same memory space in the computer.
'''
myNewVar[1] = "changed"
print("Variables (mutable2): myNewVar=", myNewVar,"myVar=", myVar)

