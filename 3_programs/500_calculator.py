'''
    As a carry over from functions and divide and conquer, this application creates a very 
    basic, text based, calculator that works on numbers and operators. 

    It should be able to accept inputs such as:

        (5+2) * 9
        ((2%3 * 7) - (87 / 14)) + 21 - (34 * 7 / 3)
        10 + 5 * 7 - 89
        etc...
    
    Inputs are limited to:
        Parenthesis separating calculations
        Integer or Float values
        Operators = %, ^, *, /, +, -

    When considering how to do this we need to look at what are the order of operations
    for doing mathmatical equations:
        1. Execute within a parameter first
            EX: (5+2) * 9
                First we must solve the parenthesis (5+2) = 7
                Then we solve 7 * 9
            EX: ((5+2) * (4+5))
                Solve the inner parenthesis
                    5+2 = 7
                    4+5 = 9
                Then solve (7*9)
        2. Operators (*,+,-, etc) have an order in which to execute

    This seems simple, right? Well it takes a bit of massaging to get it done. There are 
    a lot of steps so lets list them out:

    1. Find all of the parenthesis and solve them in proper order
    2. Execute the contents of the parenthesis 
        a. If nested, do all the nested calculations first
    4. Replace the results of the parenthesis back into the original equation
    5. Solve the original equation 

'''

'''
    Set up operations for the calculator, you can add more or 
    less depending on what you want to do. 
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

calculator_operations = {
                   '%' : mod,
                   '^' : square,
                   '*' : mult,
                   '/' : div,
                   '+' : sum,
                   '-' : sub,
                }

class Calculator:
    '''
        The calculator class takes in an equation (string), and a 
        dictionary of operations (key=char, val=fn).

        Internally the calculator will dissasemble the string into parts
        then solve the equation. 

        To do so, call resolveEquation()
    '''
    def __init__(self, equation, requested_operations):
        self.equation = equation
        self.disassembledEquation = []
        self.result = None
        self.operations = requested_operations


    def resolveEquation(self):
        self._disassembleEquation(self.equation)
        reduced_equation = self._resolveParenthesis()
        self.result = self._calculateResult(reduced_equation)
        return self.result

    '''
      Private helpers to parse equation to a list of usable items.
    '''
    @staticmethod
    def _getNumber(str_input):
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
    
    def _disassembleEquation(self, equation_as_string):
    	'''
            Parse the original equation into separate parts in which each 
            list item is either a:
                integer, float, operator, parenthesis
    
    		This function breaks down that string into a list of strings. 
    
    		For example:
                Example 1:
    			    9 + 100.9 * 7 would return [9, '+', 100.9, '*', 7]
    
                Example 2:
    			    (9 + 100.9) * 7 would return ['(', 9, '+', 100.9, ')', '*', 7]
    		PARAMETERS:
    			input_string : The raw equation
    		
            NOTES:
                Uses static _getNumber function to modify inputs to actual numbers.

    		RETURNS:
    			The input_string broken down into a list of it's parts. 
    	'''
    	return_arr = []

    	'''
    		Create an array of items from the input string as long as it's
    		not any space character.
    	'''
    	input_arr = [x for x in equation_as_string if not x.isspace()]
    
    	buffer = ''
    	for char in input_arr:
    		if not char in self.operations.keys() and not char in ['(', ')']:
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
    			if buffer:
    				return_arr.append(Calculator._getNumber(buffer))
    			return_arr.append(char)
    			buffer = ''
    
    	'''
    		If the buffer still has a value, which in most cases it will, 
    		add it as the last item in the list. 
    	'''
    	if buffer:
    		'''
    			Leftovers are NOT guaranteed to be a number
    		'''
    		try:
    			return_arr.append(Calculator._getNumber(buffer))
    		except:
    			return_arr.append(buffer)
    
    	'''
    		One final check, make sure paren counts are equal
    	'''
    	if return_arr.count(')') != return_arr.count('('):
    		raise Exception("Parenthesis count do not match")
    
    	self.disassembledEquation = return_arr
    	return return_arr

    '''
        Private helper to resolve parenthesis
    '''
    def _resolveParenthesis(self):
        '''
            Solve each of the parethesis starting from the left to right. 

            This is done by 
                1. Find  a closing parenthesis index
                2. Back up from that index to the first open parenthesis. 
                3. Capture what's there in a sub list as sub equation. 
                4. Solve the sub equation 
                4. Replace the original list items, from open to close parenthesis, with the solution to sub equation. 
        '''
        private_disassembled_equation = None

        if self.disassembledEquation:
            private_disassembled_equation = self.disassembledEquation.copy()
            while ')' in private_disassembled_equation:
                # Step 1
                close_idx = private_disassembled_equation.index(')')

                # Step 2
                open_idx = close_idx - 1
                while open_idx >= 0:
                    if private_disassembled_equation[open_idx] == '(':
                        break
                    open_idx -= 1

                if open_idx < 0:
                    raise Exception("Formatting error, cannot find opening parenthesis")

                # Step 3
                sub_equation = private_disassembled_equation[open_idx + 1: close_idx]

                # Step 4
                sub_equation_result = self._calculateResult(sub_equation)

                # Step 5
                del private_disassembled_equation[open_idx : close_idx + 1]
                private_disassembled_equation.insert(open_idx, sub_equation_result)

        return private_disassembled_equation

    '''
        Private helper to calculate results
    '''
    @staticmethod
    def _getIndexes(sequence, obj):
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

    def _calculateResult(self, equation_list):
        '''
            Calculating the final results. This function will calculate
            the results of a simple (no parethesis) equation 
    
            PARAMETERS:
                equation_list : List of numbers and operations
            
            RETURNS:
                Either an int or float value of the calculation of the input.  
        '''
        list_copy = equation_list.copy()
    
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
        for op_id in self.operations:
            '''
                Get the operation indexes then reverse them. We do that 
                because we are going to destructively work on the list. 
    
                This means if we work on the end of the list first. If we 
                started at the head of the list to do this the follow on 
                indexes would not align. 
            '''
            idxs = Calculator._getIndexes(list_copy, op_id)
            idxs.reverse()
            for idx in idxs:
                right = idx + 1
                left = idx - 1
                op_fn = self.operations[op_id]
    
                '''
                    We looked up the operation function above. Now call it 
                    with the left and right arguments and get the result. 
                '''
                result = op_fn(list_copy[left], list_copy[right])
    
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
    USE CALCULATOR
'''

'''
UNIT TESTING 
user_input = [ 
    "((100.0 + 5) - (6 + 10)) * (2.5 + 3)",
    "(2^2*4)+(4%2*9)",
    "((2%3 * 7) - (87 / 14)) + 21 - (34 * 7 / 3)"]

for input in user_input:
    calc = Calculator(input, calculator_operations)
    calc.resolveEquation()
    print(calc.equation, '=', calc.result)

    print("")
'''

'''
    ACTUAL USAGE
'''
while True:
    print("")
    user_equation = input("Enter Equation: > ")

    if user_equation in ['q','Q','quit', 'Quit']:
        print("Thanks for using Calculator")
        break

    calc = Calculator(user_equation, calculator_operations)
    calc.resolveEquation()
    print(calc.equation, '=', calc.result)
