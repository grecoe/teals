from enum import Enum

'''
    Enumerator passed into the printOutput() function so we 
    can figure out what to print. 
'''
class OutputOption(Enum):
    tomb = 1
    hello = 2

'''
    ASCII Art to output
'''
__tombstone_output = '''
        ------
       /       \\
       | R.I.P |
       |       |
       ---------
    '''

__hello_output = '''
    |   | ---------
    |   |     |
    |---|     |
    |   |     |
    |   |     |
    |   | ---------
    '''

'''
    Dictionary of images so we can quickly access them. 
'''
output_images = {
    OutputOption.tomb.value : __tombstone_output,
    OutputOption.hello.value : __hello_output
    }

'''
    Function to print out ASCII art to the screen based on an enumerator 
    in OutputOption. 

    Checks that it's actuall an instance of OutputOption and that the image 
    type is actually supported. 
'''
def printOutput(output_option):
    global output_images

    if output_option.__class__.__name__ != "OutputOption":
        print("You've done something wrong!")
    elif output_option.value not in output_images.keys():
        print("Undefined image request")
    else:
        print(output_images[output_option.value])