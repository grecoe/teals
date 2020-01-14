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
    Supported operations with order in order.
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
        Find all of the indexes of 'obj' in sequence and 
        return as a list of integers into sequence.
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
'''
def getParenPairs(sequence):
    '''
        First find all of the parenthesis and break them 
        up into their logical sets, including those contained in
        others so they are all property paired.
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
        Using the result from getParenPairs, build a heirarchy
        that will let us know if there are embeded paren pairs
        in an outer paren pair. 

        Results is a dictionary with
            key = tuple of original order (starting at 0) in which to operate on them
            values = list of Start/End of the paren. If embeded parens
                     then the list contains more than one. 
    '''
    heirarchy = {}
    pair_lists = paren_pairs.copy()

    while len(pair_lists):
        if len(pair_lists) == 1:
            heirarchy[(pair_lists[0][0],pair_lists[0][1])] = []
            pair_lists.pop(0)
        else:
            start = pair_lists.pop(0)
            idx_remove = []
            for i in range(len(pair_lists)):
                if pair_lists[i][0] > start[0] and pair_lists[i][1] < start[1]:
                    idx_remove.append(i)

            # was start[0] whereever this appears
            heirarchy_index_tuple = (start[0], start[1])
            if len(idx_remove) == 0:
                heirarchy[heirarchy_index_tuple] = [start]
            else:
                idx_remove.reverse()
                heirarchy[heirarchy_index_tuple] = []
                for idx in idx_remove:
                    heirarchy[heirarchy_index_tuple].append(pair_lists.pop(idx))
    
    # Since we popped in reverse, we need to reverse them here
    for key in heirarchy.keys():
        heirarchy[key].reverse()
    return heirarchy

def replaceParenContent(orig_text, results):
    '''
        Results are a dictionary that is
        KEY = tuple(startidx, endidx) -> Indexes of where parenthesis are
        VALUE = Value of calculated parenthesis data
    '''
    result_keys = list(results.keys())
    result_keys.reverse()
    actual_calc = "{}".format(orig_text)
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
    return_equation = user_input

    '''
        See if there are parenthesis and break them down.
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
                '''
                sub_results = {}
                master_set = user_input[part[0] + 1: part[1]]
                for sub_part in paren_heirarchy[part]:
                    working_set = user_input[sub_part[0] + 1: sub_part[1]]
                    simple_list = inputAsList(working_set)
                    paren_result = calculateResult(simple_list)
                    sub_results[(sub_part[0], sub_part[1])] = paren_result

                '''
                    Now with those sub results, solve the entire nested
                    parenthesis as an equation
                '''
                actual_calc = "{}".format(master_set)
                actual_calc = replaceParenContent(actual_calc, sub_results)

                '''
                    With the equation, now solve the most outer parenthesis
                    and save the results for later.
                '''
                simple_list = inputAsList(actual_calc)
                paren_result = calculateResult(simple_list)
                results[part] = paren_result
            else:
                # Single parenthesis in one
                working_set = user_input[part[0] + 1: part[1]]
                simple_list = inputAsList(working_set)
                paren_result = calculateResult(simple_list)
                results[part] = paren_result

        return_equation = replaceParenContent(user_input, results)

    return return_equation



'''
    Step 2: Break input into lists for calculation
'''
def inputAsList(input_string):
    global operations
    return_arr = []
    input_arr = [x for x in input_string if not x.isspace()]

    buffer = ''
    for char in input_arr:
        if not char in operations.keys():
            buffer += char
        else:
            return_arr.append(buffer)
            return_arr.append(char)
            buffer = ''

    if buffer:
        return_arr.append(buffer)

    return return_arr

'''
    Step 3: Ability to calculate results
'''
def getNumber(str_input):
    return_value = None
    try:
        return_value = int(str_input)
    except:
        return_value = float(str_input)
    return return_value

def calculateResult(sequence_list):
    global operations
    list_copy = sequence_list.copy()

    # First find all ops in order
    for op_id in operations:
        idxs = getIndexes(list_copy, op_id)
        idxs.reverse()
        for idx in idxs:
            right = idx + 1
            left = idx - 1
            op_fn = operations[op_id]


            result = op_fn(getNumber(list_copy[left]), getNumber(list_copy[right]))

            print("Calculating : {} {} {} = {}".format(list_copy[left], op_id, list_copy[right], result))

            # perform op
            list_copy.pop(right)
            list_copy.pop(idx)
            list_copy[left] = result

    # Will be broken down to a single entry
    return list_copy[0]




'''
    With all of the functionality contained in the functions above, we can simplify
    our code to actually perform the solving part. 

    Below we solve for 3 different equations. 
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
