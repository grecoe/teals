'''
    The for loop allows you to continue to execute statements while iterating over some sort of 
    sequence of items.

    Now, coming soon we will talk about the list object, but a string is also a sequence of items. 
    Those items are characters.  

    for <item> in <sequence> :
        <statements>

    Now, in this case <item> is just a variable name. You can give it any name you want, it's 
    not special assuming you don't choose a reserved Python keyword (in which you'll get an 
    error anyway). Just put any name here that, for you, makes sense. 

    As mentioned in while loops, the 'break' statement is also valid here. You can 'break' out of 
    a for loop any time you want. 
'''

'''
    range() is a built in function in Python. It returns us a sequence of numbers. If we 
    provide just one integer argument our sequence will be 0-(N-1). For example

    range(3) -> (0,1,2)

    But a range item IS a sequence that can be iterated over with a for loop. 
'''
for val in range(5):
    print(val)


'''
    A string is also a sequence. It's a sequence of characters. This means
    you can also iterate over characters in a string using a for loop. 
'''
this_is_my_name = "George Smith"
for character in this_is_my_name:
    print(character)

'''
    Break (as shown in 06_while) can be used on any condition. In this case 
    we want to go over every character in a string until we see a capital S.
'''
for character in this_is_my_name:
    if character == 'S':
        break
    print(character)
