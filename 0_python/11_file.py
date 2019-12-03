'''
    Almost all complex programs will need to read and write files. This could be 
    configuration, or data it needs to process. 

    This example will
        1. Create a text file
        2. Read a text file
        3. Remove the file we create

     Keywords:
        with, open(),os.remove()
'''
import os

localFileName = 'teals.txt'

# Create a text file. We do that by opening it for write access
# By using the 'using' keyword, the file will be closed when it loses scope
with open(localFileName, 'w') as outputFile:
    outputFile.write("The first line.\n") 
    outputFile.write("The second line.\n") 

# The file will now be closed and we can now access it for reading
with open(localFileName, 'r') as inputFile:
    lineData = inputFile.readline()
    lineNumber = 1
    while lineData:
        print(lineNumber, " = ", lineData.strip('\n'))
        lineNumber += 1
        lineData = inputFile.readline()

# Now if the file exists, we can go and delete it
if os.path.exists(localFileName):
    os.remove(localFileName)

