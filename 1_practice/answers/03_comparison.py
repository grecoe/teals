'''
    Comparisons always produce a boolean value. These are useful for if statements and
    while loops to help us create pathways in our programs to perform tasks. 

    Because it's natural to use an if statement and a while loop with comparisons, those 
    two constructs are also touched on in this file. 
'''

'''
    What is the type of result?
        class bool
    What is the value in result?
        True because 9 is less than or equal to 10
'''
result = (9 <=10 )
print("1. result = ", result)
print("1. result type = ", type(result))

'''
    What is the type of result?
        class bool
    What is the value in result?
        Normal order of operations occurs here breaking down the equation
            ( (9+1) <10 ) or (4 == 4)
            (10 < 10) or (4 == 4)
            False or True
            True
'''
result = ( (9+1) <10 ) or (4 == 4)
print("2. result = ", result)
print("2. result type = ", type(result))

'''
    What gets printed?
        Because the lower case 'a' does exist in the string 'A fat cat!', the 
        check on the if is succesful and the prited result is '3. Meow!'
'''
variable1 = 'a'
variable2 = 'A fat cat!'

if variable1 in variable2:
    print("3. Meow!")
else:
    print("3. Nothing to see here!")

'''
    What gets printed?
        Walking through the if statement, the if can't be true because 9 != 10. 
        The elif part is also false because 10 ! < 9, so since there are no 
        other checks and there is an else statement, that executes and prints

        "4. What happened to the cat?"
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
        We can walk through the while loop and write down what happens at each iteration. For iteration we
        will consider the values of the variables when the while loop expression is evaluated.. 

        Iteration   variable1   variable2
            1           0           1
            2           1           2
            3           3           5*
            4           24          12 <-- Final output
            
        * At this iteration on the following line, variable 1 becomes 7. The next line
          immediately following has the sum of variable1(7) and variable2(5).
            variable1 = variable1 + variable1 + 1

    What would happen if variable1 never gets to be 7?
        We would have an infinite loop as the only way to get out is when variable1 finally
        gets the value of 7. 
'''
variable1 = 0
variable2 = 1

while variable1 < variable2:
    print(variable1, variable2)
    variable1 = variable1 + variable1 + 1
    variable2 = variable1 + variable2

    if variable1 == 7:
        variable1 = variable2 * 2

print("5. Variables : ", variable1, variable2)