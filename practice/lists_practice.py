import os

def pause(message = '\nEnter to continue....', clear = True):
    input(message)
    if clear: 
        os.system('cls')

def listSummary(printedList):
    print("\nIf the current list looks like this: ", printedList)
    print("What will the answer be?\n")


os.system('cls')

# Create
print("1. Create a list of strings\n")
print("stringList = ['first', 'second', 'third']\n")
stringList = ['first', 'second', 'third']
pause("", False)
print("Initial List:",stringList)
pause()

# len()
print("2. What is the length of the list?\n")
print('stringLength = len(stringList)')
listSummary(stringList)
stringLength = len(stringList)
pause("", False)
print("List Length:",stringLength)
pause()

# Basic index
print("3. What is the first element?\n")
print('firstElement = stringList[0]')
listSummary(stringList)
firstElement = stringList[0]
pause("", False)
print("First Element:",firstElement)
pause()

# append()
print("4. Add one element to a list\n")
print('stringList.append("fourth")')
listSummary(stringList)
stringList.append("fourth")
pause("", False)
print("Add List:",stringList)
pause()

# extend()
print("5. Add multiple elements to a list\n")
print("subList = ['fifth','sixth','seventh']")
print('stringList.extend(subList)')
listSummary(stringList)
subList = ['fifth','sixth','seventh']
stringList.extend(subList)
pause("", False)
print("Extend List:",stringList)
pause()

# index() / insert()
print("6. Find an index of somethign in a list then inssert after it.\n")
print("foundIndex = stringList.index('second')")
print('stringList.insert((foundIndex+1), "two-to-three")')
listSummary(stringList)
foundIndex = stringList.index('second')
stringList.insert((foundIndex+1), "two-to-three")
pause("", False)
print("Insert List:",stringList)
pause()

# pop()
print("7. Remove the last element and print what you removed\n")
print('rem = stringList.pop()')
listSummary(stringList)
rem = stringList.pop()
pause("", False)
print("Popped item", rem)
pause()

# pop(n)
print("8. Remove the second element and print what you removed\n")
print('rem = stringList.pop(1)')
listSummary(stringList)
rem = stringList.pop(1)
pause("", False)
print("Popped item", rem)
print("Popped List:",stringList)
pause()

# Possible indexes / Range
print("9. What are all the valid indexes to this list?\n")
print("range: https://www.w3schools.com/python/ref_func_range.asp")
print("All valid indexes:")
for i in range(len(stringList)):
    print("    Index", i, '=', stringList[i])
pause()

# Iterating a list with for
# https://www.w3schools.com/python/python_for_loops.asp
print("10. Iterating a list with for....\n")
for item_in_my_list in stringList:
    print(item_in_my_list)

pause()
