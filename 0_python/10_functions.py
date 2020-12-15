'''
    Functions are a way to consolidate repetative or complex code that can be called one or
    more times within your program.

    Functions should be:
        1. Well named to understand what they are doing.
        2. Documented for users of the function
        3. Perform one set of actions

    In Python you create a function using this syntax:

    def <functionName>([parameters]):
        <statements>
        [return]

    Lets break this down:
        def             - Required in Python that tells the interpreter that the following
                          text is a function.
        <functionName>  - The name you give to your function. This is any name you want to give it,
                          however, it cannot be a reserved Python keyword. Function names should
                          give an indication about what the function is going to do.
        [parameters]    - Parameters are not required for a Python function. If you provde parameters
                          there can be 1 or many. If there are more than one they need to be separated
                          by commas.
        <statements>    - The Python code to execute when the funciton is called.
        [return]        - You can return 0 - many values from the function.

    NEW KEYWORD: tuple
        A tuple is another Python type that is used pretty frequently. You create a tuple by
        assigning a variable with parenthesis with a comma separated list of values.

        This sounds familiar to lists correct? You even access items in a tuple using indexes
        and a tuple IS a sequence that can be used in a for loop.

        The difference here that a tuple is an immutable object. That is, once the tuple is
        created you cannot change it.

        This is mentioned here as functions returning multiple values will return a tuple unless
        otherwise denoted (like making a list to return)
'''

'''
    Here we define a basic function that simply prints to the console.

    It takes no parameters and returns nothing.

    Then we call the function, which will make the code in the function execute.
'''
def printSomething():
    print("Basic function ")

print("1. Calling a basic function")
printSomething()





'''
    Now we will create a more complex function in that it takes two parameters
    and returns the sum of the two passed in values.
'''


def sum(parameter1, parameter2):
    return parameter1 + parameter2

print("2. Calling the sum function and getting the return value")
sum_result = sum(10,10)
print("Function result: ", sum_result)


'''
    At this point, we know the syntax of a function and that it can take 0-N
    parameters and return 0-N results.

    Passing in multiple parameters is straight forward, we provide a comma separated
    list of values. But how do we return multiple values?

    This can be done in a number of ways, and that is really up to the creator
    of the function. However, here are some strategies.
'''

'''
    Multiple return values using a list
'''
print("3. Multiple Return Values - list")
def multipleReturnValuesInAList():
    '''
        This funciton will return multiple values as a list.
    '''
    return [1,2,3,4]

list_return = multipleReturnValuesInAList()
print("multipleReturnValuesInAList returned", list_return)

'''
    Multiple return values using a dictionary
'''
print("3.1 Multiple Return Values - dictionary")
def multipleReturnValuesInADictionary():
    '''
        This funciton will return multiple values as a dictionary.
    '''
    return {1 : "first", 2 : "second"}

dict_return = multipleReturnValuesInADictionary()
print("multipleReturnValuesInADictionary returned", dict_return)

'''
    Multiple return values using tuple as default

    Returning values as a tuple is simply returning multiple objects
    as a comma separated list.

    You can call the function with a matching number of comma separated
    variables and each will be assigned a value from the function return call
    or you can simply get the tuple and iterate over the return values.
'''
print("3.2 Multiple Return Values - tuple")
def multipleReturnValuesInATuple():
    '''
        This funciton will return multiple values as a tuple.
    '''
    return 1, "first", "elephant"

print("3.2.1 Multiple Return Values - catch tuple")
tuple_return = multipleReturnValuesInATuple()
print("multipleReturnValuesInATuple returned: ", type(tuple_return), " = ",  tuple_return)

print("3.2.1 Multiple Return Values - catch comma separated values")
first, second, third = multipleReturnValuesInATuple()
print("multipleReturnValuesInATuple returned values: ", first, second, third)
