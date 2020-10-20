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
        del             - Remove a sub set of items from a list
        in              - Does an element exist in the list?
'''

'''
    Section 1 - Creating a list

    You create a list simply by creating a variable and assinging  square brackets [] to it.

    In Python the square brackets indicate a list object is being created. You can also optionally
    seed the list with values.
'''
names = ['Fred', 'Susan', 'Sally']
print("1. - Creating a list")
print( names)

'''
    Section 2 - Accessing content in a list

    So now that we have a list, how do you access the items in it?

    Well, if you want to iterate over ALL of the items in a list you could just use a for loop.
    Why, because list is just a sequence of Python objects.

    However, you may want to access a specific item in a list. To do that you use an index. This
    just means we want to point to a specific item in the list.

    Indexes on a list start at 0. That is, the first item in the list is at index 0. This means
    that the last valid index in the list is len(list) -1. Again, why? well visually, if we create
    a list of integers starting at 0 that is 5 long :

    my_list = [0,1,2,3,4]

    That list has 5 items. The first index is 0 and the last index is 4.

    A handy default function from Python is len(). You provide len() with a sequence and
    it will return how many items are in it. So for a list we can find out how long it is by

    my_list_length = len(my_list)
'''
print("2. Indexes - for loop iteration")
for name in names:
    print(name)

print("2.1 Indexes - the first item in the list")
print(names[0])

print("2.2 Indexes - the last item in the list")
print(names[len(names)-1])

'''
    Python also allows negative indexing. The negative numbers start at the first valid
    index (0). So an index of -1 means we move backwards to the end of the list and gives
    us the last item in the list.
'''
print("2.3 Indexes - the last item in the list with negative index")
print(names[-1])

'''
    A unique feature in Python is that we can collect a subset of items from a list
    using a special indexing feature.

    sub_list = item_list[start:end]

    This will get us all of the items in the list from list item_list[start] up to
    item_list[end-1].

    That is, the return list is inclusive of items from index 'start' to the one before 'end'
'''
subListOfNames = names[0:2]
print("2.4 Indexes - getting a sub list from a list")
print(subListOfNames)


'''
    Section 3 - Changing an item in a list

    To change an existing item in the list to a new value, you simply use the index of
    the item yo want to change and assign it a new value.

    This example we just change the first item in the list to 3.

    my_list[0] = 3

    Doing a straing change is easy, but most times you need to change a specific item in a list.
    So, how do you find the item you want to change? You can iterate over it, or use the
    list funciton index() function which takes a single argument. That argument is the
    item you are trying to find in the list and returns the index of the first item that
    matches it.

    For this example lets try and find 'Fred' and then replace that value with 'Gerald'. But
    we should also introduce the keyword 'in'.

    in is a way of simply asking a question of a sequnce - " is value_a in the sequence". The
    return value is just a boolean value indicating if it is in the sequence or not.

    So, first we will check to see if the list actually has a 'Fred'. If it does, we will get
    the index of 'Fred' and change it to 'Gerald'
'''
print("3 Changing list values - Find Fred")
if 'Fred' in names:
    fred_index = names.index('Fred')
    names[fred_index] = 'Gerald'
print(names)


'''
    Section 4 - Adding items to a list

    Because lists are a sequence of items you will almost always want to change
    the list by adding items to it.

    Additions can happen with several types of operations.
        append() - add a new item to the end of the list
        insert() - put an item into the list
        extend() - add another list to the end of the list
'''

'''
    We can add a new item to the end of the list with append()
'''
names.append("Joe")
print("4. Adding -  Adding an item to the end of the list")
print(names)

'''
    Insert takes an index on where to add a new item to the list. Of course,
    it has to be a valid index (which we discussed at the beginning of this topic).

    For this example lets replace the first item in the list with the value 'Mary'
'''
names.insert(0, "Mary")
print("4.1 Adding - Insert a new item at the start of the list.")
print( names)

'''
    The last way to add to a list is to use the list function extend().

    Extend just adds one list to the end of the calling list.
'''
myNewNamesList = ["Jenson", "Lewis", "Carolyn"]
names.extend(myNewNamesList)
print("4.1 Adding - Extend the list with another")
print(names)

'''
    Section 5 - Removing items from a list

    When you program starts processing a list we may also want
    to remove items from a list.

    Deletions can happen with two types of operations.
        pop() - remove a specific item from the list
        del my_list[a:b] - Remove a subset of the list
'''

'''
    Pop has an optional argument, an index.

    If you provide pop() with an index, the index must be a valid list
    index and that item will be removed from the list.

    If you do not provide pop() with an index it removes the last item
    in the list.

    pop() returns the item from the list that was removed.
'''

print("5 Deleting - pop the last item from the list")
removed_item = names.pop()
print("Removed :", removed_item, "now list is: ", names)

print("5.1 Deleting - pop the first item from the list")
removed_item = names.pop(0)
print("Removed :", removed_item, "now list is: ", names)

print("5.2 Deleting - delete a subset of the list")
del names[0:2]
print(names)
