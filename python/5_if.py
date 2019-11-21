'''
    Now that we know a litte about comparisons and understand what a boolean is it's time to put 
    some structure around it. 

    In programming, just like every day life, we need to make decisions on what to do. For example, 
    If the door is closed, open it...
    
    The 'if' statment is common in all programming languages and Python is no different. 

    The most basic if statment looks like this:

       if <expr> :
            <statements>

    So break it down. 
        <expr>      :   A value or a boolean. For now, lets just say it's a boolean value.
                        So, if the expression is True we will continue with the if statment, otherwise
                        we bypass the <statements>.
        <statements>:   Any valid python code, this code is ONLY executed if the <expr> is True.

    But what if there are more than one thing to do? What if we want to do something ONLY if 
    <expr> is False? Well the full if statment definition is the following:

       if <expr1> :
            <Execute statements if expr1 is true>
       elif <expr2> :
            <Execute statements if expr2 is true>
       else :
            <Execute statements if expr1 and expr2 are both false>

    NOTE:
        The only required part of an if statement is the if part. Elif and else are just
        optional. 

        Also note that you can make the <expr> part of an if or elif using comparisons or ANYTHING
        that produces a boolean value. So good things to review:

            1_boolean.py
            4_comparisons.py

    Keywords:
        if, elif, else
'''

doorOpen = True
windowOpen = False

# Basic operation
if doorOpen:
    print("Going out the door")


# More complex where none of the expressions are true, so shut the door first.
doorOpen = False

if doorOpen:
    print("Going out the door")
elif windowOpen:
    print("Going out the window")
else:
    print("Ugh.... I'm stuck!")