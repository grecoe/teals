'''
    Practice with lists!

    Because iterating lists lends itself to the for loop, that is covered here as well. 
'''

'''
    Create a list that will be used for the rest of this section. If you don't 
    remember, go back to 0_python\08_list.py.
'''
test_list = ["this", "is", "a", "test", "list"]

'''
    Write the code to use a for loop to print out each item in the list. 
'''
for list_item in test_list:
    print(list_item)


'''
    Write the code to determine how many items are in test_list
'''
print("1. test_list is ", len(test_list) , "in size")

'''
    What are the valid indexes into test_list to access, or change 
    a value in the list?

    ANSWER:
        The list contains 5 items and we know that valid indexes to 
        a list are 0 -> len(list)-1, so the valid indexes are 

        0,1,2,3,4
'''


'''
    How would you get the first item in the list using an index?
    How would you get the last item in the list using an index?
    Write the code for both questions.
'''
print("3. The first item in test_list is", test_list[0])
print("3. The last item in test_list is", test_list[len(test_list)-1])
print("3. The last item in test_list is", test_list[-1])

'''
    Write the code to change the value of the second item in your list to "dog".
    Print out the list to see if you changed the right item.
'''
# Second item has index 1
test_list[1] = "dog"
print("4. Change a value - ", test_list)

'''
    Write the code to remove the last item from the list.
    Write the code to remove the first item from the list. 
    Print out the list.
'''
test_list.pop()
test_list.pop(0)

print("5. Remove first and last - ", test_list)