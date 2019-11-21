import os

def pause(message = '\nEnter to continue....', clear = True):
    input(message)
    if clear: 
        os.system('cls')

def dictionarySummary(printedList):
    print("\nIf the current dictionary looks like this: ", printedList)
    print("What will the answer be?\n")

os.system('cls')

# Create
print("1. Create a dictionary\n")
print("testDictionary = {'first' : 'first_item', 'second': 2, 'third': []}\n")
testDictionary = {'first' : 'first_item', 'second': 2, 'third': []}
pause("", False)
print("Initial Dictionary:",testDictionary)
pause()

# len() - Works on dictionaries as well
print("2. What is the length of the dictionary?\n")
print('dictLength = len(testDictionary)')
dictionarySummary(testDictionary)
dictLength = len(testDictionary)
pause("", False)
print("Dictionary Length:",dictLength)
pause()

# [] index get value
print("3. Get an object from the dictionary by key\n")
print("dictEntry = testDictionary['second']")
dictionarySummary(testDictionary)
dictEntry = testDictionary['second']
pause("", False)
print("Value at 'second':", dictEntry)
pause()

# [] index set a value
print("4. Add an object to a dictionary.\n")
print("testDictionary['foobar'] = 2.0")
dictionarySummary(testDictionary)
testDictionary['foobar'] = 2.0
pause("", False)
print(testDictionary)
pause()

# Delete an entry with del 
print("5. Remove an entry with del.\n")
print("del testDictionary['third']")
dictionarySummary(testDictionary)
del testDictionary['third']
pause("", False)
print(testDictionary)
pause()

# Delete an entry with pop(key, defaultValue) 
print("6. Remove an entry with pop.\n")
print("removed_item = testDictionary.pop('second')")
dictionarySummary(testDictionary)
removed_item = testDictionary.pop('second')
pause("", False)
print("Removed - ", removed_item)
print(testDictionary)
pause()

# Delete a non-existent entry with pop(key, defaultValue) 
print("7. Remove an entry with pop.\n")
print("removed_item = testDictionary.pop('idontexist','sorry')")
dictionarySummary(testDictionary)
removed_item = testDictionary.pop('idontexist','sorry')
pause("", False)
print("Removed - ", removed_item)
print(testDictionary)
pause()

# Delete a non-existent entry with pop(key, defaultValue) 
print("8. Iterating a dictionary by key value.\n")
for key in testDictionary.keys():
    print("Key = ", key, "\t Value = ", testDictionary[key])

pause()