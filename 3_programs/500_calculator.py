'''
    As a carry over from functions and divide and conquer, this application creates a very 
    basic, text based, calculator. 

    It should be able to accept inputs such as:

        10 + 5 * 7 - 89
        ((2%3 * 7) - (87 / 14)) + 21 - (34 * 7 / 3)
        etc...
    
    Inputs are limited to:
        Parenthesis separating calculations
        Integer or Float values
        Operators = %, ^, *, /, +, -

    When considering how to do this we need to look at what are the order of operations
    for doing mathmatical equations:
        1. Execute within a parameter first
        2. Operators (*,+,-, etc) have an order in which to execute

    This seems simple, right? Well it takes a bit of massaging to get it done. There are 
    a lot of steps so lets list them out:

    1. Find all of the parenthesis
    2. Order all of the parenthesis together in pairs 
    3. Execute the contents of the parenthesis 
        a. If nested, do all the nested calculations first
    4. Replace the results of the parenthesis back into the original equation
    5. Solve the equation 

'''
from enum import Enum
from operator import itemgetter

'''
    The functions of our calculator. These are tied to an 
    operator.

    When the operator is found the associated function below
    is called. 
'''
def sum(left,right):
    return left + right
def sub(left,right):
    return left - right
def mult(left,right):
    return left * right
def div(left,right):
    return left / right
def mod(left,right):
    return left % right
def square(left,right):
    return left ** right

'''
    The mapping between operators and functionality. 

    Currently this uses the anticipated math 'operators' but really
    you could map whatever you want. 
'''
operations = {
    '%' : mod,
    '^' : square,
    '*' : mult,
    '/' : div,
    '+' : sum,
    '-' : sub,
}

'''
    General functionality used in several places
'''
def getIndexes(sequence, obj):
    '''
        Python allows you to find an object in a sequence with the 
        index() funciton. However, for parenthesis we want to find 
        ALL of the indexes of particular characters.

        For this application, particularly '(' and ')' so we can
        break down an equation. 

        This function, however, remains generic and could be used in 
        other projects.

        PARAMETERS:
            sequence : A Python sequence to search
            obj : An object in the sequence to find all indexes of in 
                  the provided sequence.

        RETURNS:
            A list of indexes in which obj was found in sequence. 
    '''
    
    indexes = []
    sub_seq = sequence
    while obj in sub_seq:
        cur_idx = sub_seq.index(obj)
        additional_idx = 0 if len(indexes) == 0 else indexes[-1] + 1
        indexes.append(cur_idx + additional_idx)
        sub_seq = sub_seq[cur_idx + 1:]

    return indexes

'''
    Step 1 : Figure out if there are parenthesis in the 
             equation and get the heirarchy of them since
             parenthesis are evaluated first.

             Then, evaluate the parenthesis and return the result

        Sub Steps: 4
'''
def getParenPairs(sequence):
    '''
        The first step in solving any equation is to determine if there 
        are parenthesis in the equation. Sub equations, found inside of 
        a set of parenthesis, will need to be solved first. 
        
        This function finds all sets of parenthesis that are aligned in 
        any order. For example:
        
        AB  BA C  C
        ((eq))+(eq)
        0123456789[10]

        The pairs returned are for A (0,5), B (1,4) and C (7,10)

        PARAMETERS:
            sequence : A python sequence to find all parenthesis pairs, for this
                       program, sequence will be a string. 

        RETURNS:
            A sorted list of paren pairs by indexes. From the above example the 
            order of return would be A,B,C as A starts before C and so on. 

        NOTE:
            If the number of open and closed parens do not match an exception is
            thrown. 
    '''
    op = getIndexes(sequence,  '(')
    cl = getIndexes(sequence,  ')')
    return_sequence = None

    if len(op) != len(cl):
        '''
            Not equal number of open/closes
        '''
        raise Exception("Formatting error, open/close paren count doesn't match")
    elif len(op) != 0:
        '''
            There are open/closes

            Get an open bracket..if the next open bracket is less that the close bracket
            keep looking to find the pairs. Then, once the pairs are built up, then sort them
            starting with the lowest starting number. 
        '''
        pairs = []
        while len(op):
            closed = cl[0]
            stack = []
            for i in range(len(op)):
                if op[i] < closed:
                    stack.append(op[i])
                else:
                    break
            pairs.append( [stack[-1], closed] )
            cl.pop(0)
            op.pop(op.index(stack[-1]))

        return_sequence = sorted(pairs, key=itemgetter(0))

    return return_sequence

def getParenHeirarchy(paren_pairs):
    '''
        Parenthesis heirarchy is important when solving an equation. It
        tells the user, or calculator, how the equation should be resolved.

        For example:

        EQ:  ((eq1) * (eq2)) + (eq3)
        IDX: 0123456789ABCDEFGHIJKLM

        The order in which to solve this is to find the results of the 
        parenthesis pairs. 
            1. eq1 = r1
            2. eq2 = r2
            3. eq3 = r3
            4. Equation now = (r1 * r2) + r3
            5. Now solve r1*r3 = r4
            6. Finally solve r4 + r5

        To do this, we need to order the parethesis in terms of solving for 
        mathmatical rules.

        This can be done by manually merging the two lists to determine what
        parenthesis are paired together, which is what this function does. 

        PARAMTERS:
            paren_pairs : The result of calling getParenPairs()

        RETURNS:
            A dictionary that describes the structure. In this case
            a tuple is set up as (start_index, end_index) of where 
            the paren pair starts and ends in the sequence.  

            However, since there can be embedded parenthesis, the dictionary
            conatins the outer parenthesis as the key and the embedded
            parenthesis as the sub equations contained within it.   

            From the example above the return would be:

            {
                (0,E) : [(1,5), (9,D)],
                (I,M) : []
            }

    '''
    heirarchy = {}
    pair_lists = paren_pairs.copy()

    while len(pair_lists):
        if len(pair_lists) == 1:
            '''
                If there is only one pair of parenthesis, we need 
                only to capture that one. 
            '''
            heirarchy[(pair_lists[0][0],pair_lists[0][1])] = []
            pair_lists.pop(0)
        else:
            '''
                If there are multiple pairs we need to filter through them
                to determine if there are sub equations. 

                Because we know the pairs are in ordered fashion, take the 
                head of the list and compare it to all other pairs in the list.

                If another pair is found in which both start and end parenthesis
                are contained in with in the values of the set we are checking 
                it is a sub equation. 

                Collect it and also remove it from the list.  
            '''
            start = pair_lists.pop(0)
            idx_remove = []
            for i in range(len(pair_lists)):
                if pair_lists[i][0] > start[0] and pair_lists[i][1] < start[1]:
                    idx_remove.append(i)

            '''
                Create the main tuple to be added to the results. 

                IF idx_remove is empty, then there were no sub equations
                and we can simply add it to the results dictionary.

                ELSE we add every sub tuple to the dictionary under the main
                tuple.  
            '''
            heirarchy_index_tuple = (start[0], start[1])
            if len(idx_remove) == 0:
                heirarchy[heirarchy_index_tuple] = [start]
            else:
                idx_remove.reverse()
                heirarchy[heirarchy_index_tuple] = []
                for idx in idx_remove:
                    heirarchy[heirarchy_index_tuple].append(pair_lists.pop(idx))
    
    '''
        We popped from the list in which we reveresed it first to not 
        run into issues when destroying the list in the first place. 

        Reverse our results, if any, under each tuple key so that they 
        are now in order from left to right.
    '''
    for key in heirarchy.keys():
        heirarchy[key].reverse()

    return heirarchy

def replaceParenContent(orig_equation, results):
    '''
        According to the rules we described earlier, parenthesis sub equations
        must be resolved first. 

        This function resolves those sub equations and replaces the result in 
        the original text. 

        PARAMETERS:
            orig_equation : String representing the original equation that contains
                            parenthesis holding sub equations. 
            results:        A dictionary that contains a:
                            KEY: (start_idx, end_idx) identifying the start and end 
                                 of parenthseis to replace.
                            VALUE: The value calculated from the sub equation. 
        
        RETURNS:
            A string of the modified origin_equation with the parenthesis enclosed
            equations resolved and all parenthesis removed. 

            For example:
            Orig Equation: (7+4) * (9-1)
            Returns:        11 * 8
    '''
    result_keys = list(results.keys())
    result_keys.reverse()
    actual_calc = "{}".format(orig_equation)
    for key in result_keys:
        '''
            Account for the first character being the open paren
        '''
        sub_calc = ''
        if key[0] > 0:
            sub_calc = actual_calc[0:key[0]-1]

        sub_calc += str(results[key])
        if (len(actual_calc) -1) > (key[1] + 1):
            sub_calc += actual_calc[key[1] + 1:] 
        actual_calc = sub_calc

    return actual_calc

def resolveParenthesis(user_input):
    '''
        This function is the outer most function to deal with parenthesis and 
        makes use of all the above functions to do it's work. 

        PARAMETERS:
            user_input: The original equation entered to resolve out parentheis
                        surrounded sub equations.
        
        RETURNS:
            A string representation of the reduced input equation to finally solve. 

            EX 1: Parenthesis in original equation
                input   = ((7+4) * (8-1)) + (12 / 3)
                returns = 77 + 4
            
            EX 2: No parenthesis in original equation
                input   = 1 + 2 + 3 * 8
                returns = 1 + 2 + 3 * 8
    '''

    '''
        Capture the original equation as a return value. If no 
        parenthesis are found, this will be returned. 
    '''
    return_equation = user_input

    '''
        See if there are parenthesis. If there are any then 
        paren_heirarchy will have a value and we need to break them 
        down.
    '''
    paren_heirarchy = None
    paren_pairs = getParenPairs(user_input)
    if paren_pairs:
        paren_heirarchy = getParenHeirarchy(paren_pairs)

    if paren_heirarchy:
        results = {}
        for part in paren_heirarchy.keys():
            if len(paren_heirarchy[part]) > 0:
                '''
                    Break down the nested parenthesis and solve them.

                    sub_results ends up with the paren start and end index
                    as the tuple key and the resolved equation as the value.

                    This first step breaks down any sub parts that were found
                    from the main parenthesis pair.. 
                '''
                sub_results = {}
                master_set = user_input[part[0] + 1: part[1]]
                for sub_part in paren_heirarchy[part]:
                    working_set = user_input[sub_part[0] + 1: sub_part[1]]
                    simple_list = inputAsList(working_set)
                    paren_result = calculateResult(simple_list)
                    sub_results[(sub_part[0], sub_part[1])] = paren_result

                '''
                    Now with those sub results, replace the parenthesis pairs 
                    with the results we resolved into the parent parenthesis set. 

                    The output will be the final equation of the outer parenthesis
                    that we must solve. 
                '''
                actual_calc = "{}".format(master_set)
                actual_calc = replaceParenContent(actual_calc, sub_results)

                '''
                    With the final equation, now solve the most outer parenthesis
                    and save the results.
                '''
                simple_list = inputAsList(actual_calc)
                paren_result = calculateResult(simple_list)
                results[part] = paren_result
            else:
                '''
                    This parenthesis pair has not sub equations so 
                    simply get the result for this set.
                '''
                working_set = user_input[part[0] + 1: part[1]]
                simple_list = inputAsList(working_set)
                paren_result = calculateResult(simple_list)
                results[part] = paren_result

        '''
            Now that we have resolved all parenthesis, we can take the original
            input and replace all parenthesis pairs with the actual calculated
            value. 
        '''
        return_equation = replaceParenContent(user_input, results)

    return return_equation

'''
    Step 2: Break input into lists for calculation
        Sub Steps: 1
'''
def inputAsList(input_string):
    '''
        Once the original equation has had all the parenthesis resolved we
        are left with a basic equation with no sub equations. 

        This function breaks down that string into a list of strings. 

        For example:
            9 + 100.9 * 7 would return ['9', '+', '100.9', '*', '7']
            for future processing to get the final result. 

        PARAMETERS:
            input_string : The fully resolved (parenthesis) equation to be solved.
        
        RETURNS:
            The input_string broken down into a list of it's parts. 
    '''
    global operations
    return_arr = []
    '''
        Create an array of items from the input string as long as it's
        not any space character.
    '''
    input_arr = [x for x in input_string if not x.isspace()]

    buffer = ''
    for char in input_arr:
        if not char in operations.keys():
            '''
                Character is not one of the calculator operators so 
                collect anythign in there. This will account for float (2.5)
                or multi value (100) integers.
            '''
            buffer += char
        else:
            '''
                When we get an operator, whatever we were collecting in the 
                buffer is complete. Add that to the list and clear it. Also
                add in whatever operator we just encountered.
            '''
            return_arr.append(buffer)
            return_arr.append(char)
            buffer = ''

    '''
        If the buffer still has a value, which in most cases it will, 
        add it as the last item in the list. 
    '''
    if buffer:
        return_arr.append(buffer)

    return return_arr

'''
    Step 3: Ability to calculate results

        Sub Steps: 2
'''
def getNumber(str_input):
    '''
        Convert a string to an integer or a float. 

        PARAMETER:
            str_input : String representing an int or float

        RETURNS:
            An int or float value.
        
        NOTE:   
            If the string is in the wrong format, this function 
            will throw an exception. 
    '''
    return_value = None
    try:
        return_value = int(str_input)
    except:
        return_value = float(str_input)
    return return_value

def calculateResult(sequence_list):
    '''
        Calculating the final results. This function will calculate
        the results of a simple (no parethesis) equation that was broken
        down with the inputAsList() function.

        PARAMETERS:
            sequence_list : Result of calling inputAsList()
        
        RETURNS:
            Either an int or float value of the calculation of the input.  
    '''
    global operations
    list_copy = sequence_list.copy()

    '''
        Operations are ordered in precedence in the global operations
        dictionary. We are going:
            1. Run through each operation in order of precedence
            2. Find any indexes where they might reside
            3. Parse the array, starting at the op_index to get
                op_index -1 = Left side of operation
                op_index +1 = Right side of operation
                op_index    = The index of the operator.
            4. Resolve the operation using the function stored in the 
               global operations dictionary value using the operator 
               as the look up value. 
            5. Pop op_index and op_index + 1 to remove them from the list.
            6. Set op_index -1 to the calculated value

            We will run the aboe steps until all operations have been checked
            which will result in a list with exactly one value, the final 
            calculation.
    '''
    for op_id in operations:
        '''
            Get the operation indexes then reverse them. We do that 
            because we are going to destructively work on the list. 

            This means if we work on the end of the list first. If we 
            started at the head of the list to do this the follow on 
            indexes would not align. 
        '''
        idxs = getIndexes(list_copy, op_id)
        idxs.reverse()
        for idx in idxs:
            right = idx + 1
            left = idx - 1
            op_fn = operations[op_id]

            '''
                We looked up the operation function above. Now call it 
                with the left and right arguments and get the result. 
            '''
            result = op_fn(getNumber(list_copy[left]), getNumber(list_copy[right]))

            '''
                This line just lets the user know what we are calculating right now. 
            '''
            print("Calculating : {} {} {} = {}".format(list_copy[left], op_id, list_copy[right], result))

            '''
                Finally, remove the right and op items from the list and 
                replace the left item with the calculated value.
            '''
            list_copy.pop(right)
            list_copy.pop(idx)
            list_copy[left] = result

    return list_copy[0]




'''
    Below we solve for 3 different equations. 

    Note that by using functions to perform all of the work, the acutal 
    calculator code is brief and to the point. Exactly what we want when 
    we start debugging. 

    If there is an issue (and I'm sure there are some), we can simply check
    at each step where the issue is?

        Is it when we resolve all of the parenthesis?
        Is it when we calcualte the final result? 

    When running the program you will see how each cacluation is done and 
    in which order as it works towards solving the main equation. 
'''
user_input = [ 
    "((100.0 + 5) - (6 + 10)) * (2.5 + 3)",
    "(2^2*4)+(4%2*9)",
    "((2%3 * 7) - (87 / 14)) + 21 - (34 * 7 / 3)"]

for eq in user_input:
    print("Solving: ", eq)
    calculate_results_from = resolveParenthesis(eq)
    simple_list = inputAsList(calculate_results_from)
    print(eq, '=', calculateResult(simple_list))
    print("")
