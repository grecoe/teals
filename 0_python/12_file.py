'''
    Almost all complex programs will need to read and write files. This could be 
    configuration, or data it needs to process. 

    This example will
        1. Create a text file
        2. Read a text file
        3. Remove the file we create

    Notice that we have to import the os module which gives us access to 
    operating system calls such as os.path, os.remove, etc.
'''
import os

localFileName = 'teals.txt'

'''
    This code block uses another built in Python keyword - with

    You can read details about with here : https://docs.python.org/2.5/whatsnew/pep-343.html

    This code opens an operating system file by a given name and a given access request. This
    example opens up localFileName with write access. 

    The output of the open call assigns a file object to the variable outputFile. 

    Once in the with statement we can then write to the file, because we asked for write permission.
    When the with block completes the operating system file handle is closed.
'''
with open(localFileName, 'w') as outputFile:
    outputFile.write("The first line.\n") 
    outputFile.write("The second line.\n") 

'''
    Usnig the same type of structure as above, we ask to open the file we just created
    with read access. 

    Then we read in each line of the file until there is no more data to read.
'''
with open(localFileName, 'r') as inputFile:
    lineData = inputFile.readline()
    lineNumber = 1
    while lineData:
        print(lineNumber, " = ", lineData.strip('\n'))
        lineNumber += 1
        lineData = inputFile.readline()

'''
    The os module allows us to perform operating system functions. 

    This code determines if a particular file exists, and if so, deletes it.

    Of course, if you executed the code above, this file WILL exist.
'''
if os.path.exists(localFileName):
    os.remove(localFileName)

