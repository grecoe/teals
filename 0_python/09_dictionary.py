'''
    Dictionaries are a different construct than a list. Items are kept in a dictionary 
    using a key. 

    Visually a dictionary looks like this:

    {
        key1 : value1,
        key2 : value2,
        etc
    }

    With a list, you access items with an index. With a dictionary you access items using a 
    key value. 

    A dictionary has two sequences you can access they are 
        keys() and values()
'''


'''
    Section 1 - Creating a dictionary

    You create a dictionary simply by creating a variable and assinging  
    curly brackets {} to it.

    In Python the curly brackets indicate a dictionary object is being 
    created.
'''

'''
    You can initialize a dictionary with values by simply referencing 
    a key and giving it a value.

    Values are added as:
        key : value

    You can enter multiple of them separating the entries with a comma. 
'''
print("1. - Creating a dictionary - Initialization")
schools = { 
    'Massachusetts' : "Boston University", 
    'California' : 'UCLA', 
    "Florida" : "Florida State"
    }
print(schools)


'''
    Or, if you don't know everything you're going to add at initialization,
    you simply add by referencing a key name as an index and assign a value
    to it. 
'''
print("1.1 - Creating a dictionary - By key")
schools2 = {}
schools2['Massachusetts'] = "MIT"
schools2['California'] = "Berkley"
schools2['Florida'] = "University of Miami"
print(schools2)

'''
    Section 2 - Accessing content in a dictionary

    So now that we have a dictionary, how do you access the items in it? 

    If you want to iterate over ALL of the items in a dictionary you could 
    just use a for loop that iterates over the dictionary keys and then 
    access the values that way. 

    Remember, we access items in the dictionary indexing with a key value.  
'''
print("2. Accessing content - Iterate with keys")
for key in schools.keys():
    print(key, '=', schools[key])

print("2.1 Accessing content - Index with specific key")
print("key = 'Florida' = ", schools['Florida'])


'''
    Section 3 - Changing an item in a dictionary

    Similary to lists, we change the value of an item in a dictionary 
    with an index.

    The index here MUST be a valid key. 
'''
print("3. Changing content - Index with key")
schools['Massachusetts'] = "MIT"
print(schools)

'''
    Remember the 'in' operator in Python, you can also determine if your 
    dictionary has a value before you access to ensure you have a valid 
    key.
'''
if 'Florida' in schools.keys():
    print("3.1 Dictionary has Florida")

'''
    Section 4 - Removing items from a dictionary

    When you program starts processing a dictionary we may also want 
    to remove items from a dictionary. 

    Deletions can happen with two types of operations. 
        pop(key) - remove a specific item from the dictionary and
                   return the value at that key.
        del my_dict[key] - Remove an item from the dictionary and 
                           you will NOT get the value back.
 
'''
print("4 Deleting - pop an item from the dictionary")
popValue = schools.pop('Florida') 
print("Key Popped : 'Florida' Popped : ", popValue, "dictionary : ", schools)

print("4.1 Deleting - use del to remove an item")
del schools['Georgia'] 
print(schools)


