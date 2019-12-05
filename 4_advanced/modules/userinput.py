'''
    This file allows you to hide all of the implementation details of asking 
    a user for input for your program. It will verify that the correct data is 
    returned. 

    Externally, we want to expose the getUserInput().
'''


'''
    __parseInt

    Parameters
        userInput : Input string from user
        error : Error to display if not a int
    
    Returns:
        Int if non error, None otherwise
'''
def __parseInt(userInput, error):
    returnVal = None
    try:
        returnVal = int(userInput)
    except Exception as ex:
        returnVal = None
        print(error)
    return returnVal

'''
    __parseFloat

    Parameters
        userInput : Input string from user
        error : Error to display if not a float
    
    Returns:
        Float if non error, None otherwise
'''
def __parseFloat(userInput, error):
    returnVal = None
    try:
        returnVal = float(userInput)
    except Exception as ex:
        returnVal = None
        print(error)
    return returnVal

'''
    getUserInput:

    Parameters:
        prompt : Prompt to show to the user
        error: Error to show to the user if expected type not input.
        classInfo: Class info of type to collect
        retries: Number of times to allow user to get it right. 

    Returns:
        Expected value type if retries isn't exceeded
'''
def getUserInput(prompt, retries,  error, classInfo):

    userValue = None
    className = classInfo.__name__

    currentRetries = 0
    while True:
        currentRetries += 1

        userInput = input(prompt)

        if className == 'int':
            userValue = __parseInt(userInput, error)
        elif className == 'float':
            userValue = __parseFloat(userInput, error)
        else:
            userValue = userInput

        # If we have a value, get out
        if userValue is not None:
            break

        # If we've exhausted our retries, get out.
        if currentRetries >= retries:
            print("You have exhausted your attempts to enter a ", className)
            break

    return userValue
