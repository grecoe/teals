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
    Section 1 - Creating a list

    You create a dictionary simply by creating a variable and assinging  curly brackets {} to it.

    In Python the curly brackets indicate a dictionary object is being created. You can also optionally
    seed the list with values.

    Values are added as:
        key : value

    You can enter multiple of them separating the entries with a comma. 
'''
print("1. - Creating a dictionary")
schools = { 'Massachusetts' : "Boston University", 'California' : 'UCLA', "Florida" : "Florida State"}
print(schools)

'''
    Section 2 - Accessing content in a dictionary

    So now that we have a dictionary, how do you access the items in it? 

    Well, if you want to iterate over ALL of the items in a list you could just use a for loop 
    that iterates over the dictionary keys and then access the values that way. 

    Remember, we access items in the dictionary indexing with a key value.  
'''
print("2. Accessing content - Iterate with keys")
for key in schools.keys():
    print(key, '=', schools[key])

print("2.1 Accessing content - Index with specific key")
print("key = 'Florida' = ", schools['Florida'])


'''
    Section 3 - Changing an item in a dictionary

    Similary to lists, we change the value of an item in a dictionary with an index.

    Again, the index here must be a valid key. 
'''
print("3. Changing content - Index with key")
schools['Massachusetts'] = "MIT"
print(schools)


'''
    Section 4 - Adding items to a list

    Unlike lists there is one way to add an item to a dictionary. 

    Simplly access the dictionary with a key value and assign a value. If the key
    exists, the existing item is changed. If the key does not exist it is added 
    as a new key value pair.
'''
print("4. Adding content - Index with key")
schools['Georgia'] = 'Georgia Tech' 
print(schools)

'''
    Section 5 - Removing items from a dictionary

    When you program starts processing a dictionary we may also want 
    to remove items from a dictionary. 

    Deletions can happen with two types of operations. 
        pop(key) - remove a specific item from the list
        del my_dict[key] - Remove a subset of the list

    Note here that pop requires a valid key in the dictionary and del will remove 
    an item and also requires a valid key. The difference here is that pop will 
    return the value of the key removed where del does not. 
'''
print("5 Deleting - pop an item from the dictionary")
popValue = schools.pop('Florida') 
print("Key Popped : 'Florida' Popped : ", popValue, "dictionary : ", schools)

print("5.1 Deleting - use del to remove an item")
del schools['Georgia'] 
print(schools)


