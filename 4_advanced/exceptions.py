'''
    Exception handling is pretty important in todays modern software designs. There used to be a 
    time where programs would check every single operation before executing code. If it falied a 
    test, an error code was returned.
    
    Today, some of those tests just don't happen, such as a file being missing that was expected, or, 
    in a simple case, casting to something that doesn't work. 

    In these cases try, except , finally structures are used. These catch exceptions and the developer
    can choose to handle the exception or not. If not, they can re-throw it and hope someone else 
    catches it. If no one catches an exception, the program terminates. 

    try:
        Try to execute somethign here
    except [specific exception type or not]:
        Happens when the try fails
    finally:
        This executes no matter what happens above. 

    Hint: You can always catch a general exception and then figure out what it is so you can make 
    your exception handling better:
        catch Exception as ex:
            type(ex)
'''
print("Program started....")

try:
    int_value = int("This is not an int")
except ValueError as ex:
    print("Naughty....you cast somethign you should not have....")
    print(type(ex) , ex)
except Exception as ex:
    print("I caught an exception that wasnt a casting error!")
    print(type(ex) , ex)
finally:
    print("FINALLY -> No matter what happens I print out....")

print("Program over....")
