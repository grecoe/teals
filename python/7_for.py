'''
    The for loop allows you to continue to execute statements while iterating over some sort of 
    sequence of items.

    Now, coming soon we will talk about the list object, but a string is also a sequence of items. 
    Those items are characters.  

    for <item> in <sequence> :
        <statements>

    Now, in this case <item> is just a parameter. You can give it any name you want, it's not special
    assuming you don't choose a reserved Python keyword (in which you'll get an error anyway). Just
    put any name here that, for you, makes sense. 

    As mentioned in while loops, the 'break' statement is also valid here. You can 'break' out of 
    a for loop any time you want. 

    Keywords:
        for, break, in, range()
'''

# Range will give us N numbers (as a sequence) starting at 0. N is the input to the range call. 
# Print out the numbers in range(5) using a for loop.  
print("Range")
for val in range(5):
    print(val)


print("Use for to print out the characters in a string.")
this_is_my_name = "George Smith"
for character in this_is_my_name:
    print(character)

print("Break out if we encounter an 'S'")
for character in this_is_my_name:
    if character == 'S':
        break
    print(character)
