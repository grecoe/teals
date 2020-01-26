'''
    Comparisons always produce a boolean value. These are useful for if statements and
    while loops to help us create pathways in our programs to perform tasks. 

    Because it's natural to use an if statement and a while loop with comparisons, those 
    two constructs are also touched on in this file. 
'''

'''
    What is the type of result?
    What is the value in result?
'''
result = (9 <=10 )
print("1. result = ", result)
print("1. result type = ", type(result))

'''
    What is the type of result?
    What is the value in result?
'''
result = ( (9+1) <10 ) or (4 == 4)
print("2. result = ", result)
print("2. result type = ", type(result))

'''
    What gets printed?
'''
variable1 = 'a'
variable2 = 'A fat cat!'

if variable1 in variable2:
    print("3. Meow!")
else:
    print("3. Nothing to see here!")

'''
    What gets printed?
'''
variable1 = 10
variable2 = 9

if variable1 == variable2:
    print("4. I like your thinking!")
elif variable1 < variable2:
    print("4. Anything is possible!")
else:
    print("4. What happened to the cat?")

'''
    What are the values of variable1 and variable2 when they get printed?

    What would happen if variable1 never gets to be 7?
'''
variable1 = 0
variable2 = 1

while variable1 < variable2:
    variable1 = variable1 + variable1 + 1
    variable2 = variable1 + variable2

    if variable1 == 7:
        variable1 = variable2 * 2

print("5. Variables : ", variable1, variable2)