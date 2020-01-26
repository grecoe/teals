'''
    Variables can be in scope globally or locally, this tells you what 
    you have access to. 

    Locally available variables have a more limited scope than global variables. 
    That is, a variable declared inside of a function can only be seen within the 
    function. Once the function returns, the variable is gone. 

    Globally available variables are visible throughout your program, even inside of 
    functions. 
'''

'''
    These variables declared outside of any function are considered 'global' to the file. 
'''
first_global_variable = 1
second_global_variable = "hello"

def functionA():
    '''
        functionA() :
            Creates a local variable called function_variable and then we print out
            the variables visible at the local level. 
    '''
    print("2. Function A : Locals to Function")
    function_variable = "world"
    local_variables = locals().copy()
    for item in local_variables:
        print(item)    

def functionB():
    '''
        functionB() :
            Prints out all the varaibles that are visible globally. You will notice that
            even the functions functionA and functionB are visible. 
    '''
    print("3. Function B : Globals to function")
    global_variables = globals().copy()
    for item in local_variables:
        print(item)    

'''
    Get the local variables...they will change here when we create the for loop. 
     You will see, aside from the built in python types, we will see our two variables. 
'''
print("1. Local variables to the file...")
local_variables = locals().copy()
for item in local_variables:
    print(item)

'''
    Have a look at the local variables in functionA()
'''
print("")
functionA()

'''
    Have a look at the global variables in functionB()
'''
print("")
functionB()

'''
    We can see the global variables in a function, but to be sure you are accessing 
    the right variable you can use the keyword global in a function to ensure that
    we really are accessing the global variables. 
'''
print("")
print("4. Change global variable first_global_variable in a function : ", first_global_variable)

def changeFirstVariable():
    '''
        Declare first_global_variable as a global variable and alter it.
    '''
    global first_global_variable
    first_global_variable += 1

changeFirstVariable()
print("4.1 Modified  global variable first_global_variable in a function : ", first_global_variable)
