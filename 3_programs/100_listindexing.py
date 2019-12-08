'''
    Indexing into an array is a key concept that is important to understand 
    for using lists. 

    This example will create several lists and traverse it in many ways. 
'''

'''
    If you don't understand how the lists are being built, it's OK. All it's 
    doing is building a list of lists. Each contained list has three numbers.
    The numbers start at 0 and go to 8. 
'''
list_container = [
    [x for x in range(0,3)],
    [x for x in range(3,6)],
    [x for x in range(6,9)],
]


# Iterate over the list_container, the thing that contains lists using a for statement
print("\nThe list of lists broken down :")
for list in list_container:
    print(type(list), list)

# What are all the possible indexes (excluding negative indexes...)
print("\nAll possible indexes and what is stored there :")
for container_index in range(len(list_container)):
    print("List Container - list_container[", container_index,"] = ", list_container[container_index])
    for list_index in range(len(list_container[container_index])):
        print("    Contained List - list_container[", container_index,"][",list_index,"] = ", list_container[container_index][list_index])


# Iterate over all lists and buld up the alpabet using nothign but indexes. You can get
# all valid indexes using the range() function. 
print("\nBuild up a list containing numbers in order :")
ordered_numbers = ''
for container_index in range(len(list_container)):
    print("Using list", container_index)
    
    # Use the index to get at a contained list
    for list_index in range(len(list_container[container_index])):
        # Double index, one to get to the list, the other to index into that list
        ordered_numbers += str(list_container[container_index][list_index]) + " "

print("Numbers in order: ", ordered_numbers)

