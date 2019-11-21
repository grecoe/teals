'''
    A list is a common thing in programming. Sometimes you will hear it referred to as an 
    array. Either way, it means the same thing. 

    Think of the line when you go to the cafeteria or Dunkin Donuts. You are part of a list 
    of people waiting to get served. Lists, conceptually, are that easy. A list of items (or people, 
    or integers, or anything else)

    Lists in Python can hold ANY valid Python object and a list can be made up of a different types
    of Python objects. That is, a list doesn't always have to have the same things in it.....but 
    that is typically bad practice to do, as it makes it harder to process it.

    You access items in a list using an index (typically). The index is just an integer for the 
    position in the list you are trying to access. Unlike the lists you would write:

        The first index in a list is ALWAYS 0
        The last index in a list is ALWAYS len(list)-1 [one less than the number of elements in it] 

    There are a lot of operations you can perform on a list:
        list = []       - Create a new list
        list[X]         - Index into the list where X >= 0 and X <= len(list)-1
        index(item)     - If the 'item' is found in the list, it gets it's index
        len             - Get the length of a list
        append()        - Add a single item to the list
        insert(idx,item)- Inserts 'item' at the specified index (idx)
        extend()        - Add another list to the end of this list.
        pop([N])        - Removes an item from the list. pop() removes the last element or
                          pop(N), where N is a valid index in the list removes the item at 
                          the specified index. 
        in              - Does an element exist in the list?


    Keywords:
        [] constructor, [] indexer,  len(), index(), append(), insert(), extend(), pop()  
'''

# [] constructor
names = ['Fred', 'Susan', 'Sally']
print("1.", names)

# [] indexer
# Indexing can be interesting...in Python you can use negative numbers move backwards 
# through a list. The index -1 is the last item in the list. The index -2 is the second 
# to last item in the list and so on. 
firstName = names[0]
lastName = names[len(names)-1]
lastNameNegative = names[-1]
print("2.", firstName, lastName, lastNameNegative)

# Indexing also takes a different turn here as well using the notation list[X:Y]
# Think of it this way. 
#   Start getting items at index X. Return Y-X items. 
subListOfNames = names[0:2]
print("3.", subListOfNames)

# You can also use indexing to change the value in a list. 
names[0] = "Gerald"
print("4.", names)

# len()
print("5.", len(names))

# index() - Find index for Susan in the list
susanIndex = names.index('Susan')
print("6.", names[susanIndex])

# append() - Add Joe to the list
names.append("Joe")
print("7.", names)

# insert() - Insert Mary at where Susan is
names.insert(susanIndex, "Mary")
print("8.", names)

# extend() - Add another list to the original list
myNewNamesList = ["Jenson", "Lewis", "Carolyn"]
names.extend(myNewNamesList)
print("9.", names)

# pop() - remove the last item in the list
names.pop()
print("10.", names)

# Now remove the second name from the list
names.pop(1)
print("11.", names)

# Does somethign exist in the list?
print("12.", 'Jenson' in names)