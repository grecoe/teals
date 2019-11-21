'''
    Dictionaries are a different construct than a list. Items are kept in a dictionary 
    using a key. 

    Visually a dictionary looks like this:

    {
        key1 : value1,
        key2 : value2,
        etc
    }

    You access items in the dictionary using a key value. Keys can be various types of Python objects, 
    but it's really suggested you don't use a complex type and typically as you are learning it
    you will not have to worry about that. 

    That restriction does not hold for the values. Values can be ANY valid Python object.

    Keywords:
        {} constructor, [] key index, del, pop()
'''

# {} constructor
schools = { 'Massachusetts' : "Boston University", 'California' : 'UCLA', "Florida" : "Florida State"}
print("1.", schools)

# [] Indexing
# Get an item by a key
print("2.", schools['Florida'])
# Change an item by a key
schools['Massachusetts'] = "MIT"
print("3.", schools)

# Add an item. Simply come up with a new key name and insert it
# using indexing as well.
schools['Georgia'] = 'Georgia Tech' 
print("4.", schools)

# del - Delete an item from the dictionary using a key
del schools['Georgia'] 
print("5.", schools)

# pop() - You pop an item from the dictionary using a key as well. So why use pop 
#         instead of del? Because pop() returns the value that is being removed.
popValue = schools.pop('Florida') 
print("6.", popValue)
print("6.1", schools)

# Iterating over a dictionary. A dictionary can return it's key collection with 
# the keys() function. You can use this in a for loop as so:
for key in schools.keys():
    print("Key = ", key, "Value = ", schools[key])

# Does a key even exist?
print("7.", 'Florida' in schools.keys())