'''
    Variables can be in scope globally or locally, this tells you what 
    you have access to. 

    Keywords:
        locals(), globals()
'''

my_first_variable = 1
my_second_variable = "hello"

def functionA():
    print("Function A : Locals to Function")
    function_variable = "world"
    local_variables = locals().copy()
    for item in local_variables:
        print(item)    

def functionB():
    print("Function B : Globals to Function (which are also local when calling in global scope)")
    global_variables = globals().copy()
    for item in local_variables:
        print(item)    

# Get the local variables...they will change here when we create the for loop. 
# You will see, aside from the built in python types, we will see our two variables. 
print("Local variables to the file...")
local_variables = locals().copy()
for item in local_variables:
    print(item)

# When you get local variables in a function, you get only the variables that the function
# can see. 
print("")
functionA()

# When you get global variables in a function, you get the globals to the whole
# script, which include the names of the functions we've defined. 
print("")
functionB()

# Finally you can access global variables in your functions as long as
# you declare it in the function. 
print("")
print("Change global variable in a function")
print(my_first_variable)

def changeFirstVariable():
    global my_first_variable
    my_first_variable += 1

changeFirstVariable()
print(my_first_variable)
