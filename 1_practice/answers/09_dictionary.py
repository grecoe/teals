'''
    Practice with dictionaries!

    Because iterating dictionaries lends itself to the for loop, that is covered here as well. 
'''


'''
    Create a dictionary that will be used for the rest of this section. If you don't 
    remember, go back to 0_python\09_dictionary.py.
'''
test_dict = {"first" : "value1", "second" : "value2"}

'''
    Write the code to add two more items to the dictionary. 
'''
test_dict["third"] = "value3"
test_dict["fourth"] = "value4"
print("1.", test_dict)

'''
    Write the code to determine how many items are in test_dict
'''
print("2. test_dict is ", len(test_dict) , "in size")

'''
    Write the code to iterate over test_dict using a for loop and print
    out each key and value.
'''
print("3. Iterate dictionary")
for key in test_dict.keys():
    print(key, "=", test_dict[key])

'''
    How would you get a value from the dictionary with a key?

    ANSWER: You need to have a key to get it, dictionaries don't work with indexes.
'''
print("4.", test_dict['first'])

'''
    Write the code to change the value of any item in your dictionary to "dog".
    Print out the dictionary to see if you changed the right item.
'''
test_dict['first'] = 'dog'
print("5. Change a value - ", test_dict)

'''
    Write the code to remove any item from the dictionary. 
    Print out the dictionary.
'''
test_dict.pop('first')
print("6. Remove an item - ", test_dict)
