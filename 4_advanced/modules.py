'''
    Modules are external code objects that you can import into your project. 

    As the intro class progresses, you will have already done some imports on things 
    such as math or random. 

    You have also seen on some of my examples where I import the os module so that I 
    can clear the screen between steps in a script:
        os.system('cls')

    Modules allow you to break out your code so that your main programs are clean and 
    easy to understand. 

    You can create your own modules simply by creating a directory and:
        Create an __init__.py file so Python knows what to load 
        Create other .py files containing your code. 

    You import your module by identifying the name of the directory and the file name 
    separated by a ".".

    For example, I've created teh 'modules' directory and created a code file 
    'userinput.py'. To access that we 

    import modules.userinput

    Now if we want to just import the single function in there 'getUserInput()' 
    we change the import statement to only get that function

    from modules.userinput import getUserInput
'''

# Import the os module so we can clear the screen
import os

# Import the one function in the modules\userinput.py file
from modules.userinput import getUserInput

# Import the enum class and printOutput function from modules\useroutput.py
from modules.useroutput import OutputOption, printOutput

# Using the os module, clear the screen
os.system('cls')


'''
    Using the imported function from modules.userinput, get an integer from the 
    user. Allow them up to 3 tries.

    Try this with an float, string and finally an integer
'''
user_integer = getUserInput("Enter an integer value > ", 3, "Not an integer!", int)
print("User input was:", user_integer)
print("Data Type:", type(user_integer))


'''
    Using the imported Enum class and the printOutput() function from the module 
    modues.useroutput, print out the possible images. 
'''
print("Getting tombstone.....")
printOutput(OutputOption.tomb)
print("Getting hello....")
printOutput(OutputOption.hello)
