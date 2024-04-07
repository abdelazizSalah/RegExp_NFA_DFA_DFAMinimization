from collections import deque

class Validation: 
    def __init__(self): 
        print('calling validation')
        
    def validate_parentheses(self, expression: str) -> bool: 
        '''
        This function validates the parentheses in the expression.
        It returns True if the parentheses are valid, otherwise it returns False.
        The parantheses are valid in the following cases: 
            1. no empty parentheses either [] or ()
            2. # of '(' == # of ')' and in a correct order, same for []. 

        Input: 
            expression: str
        Output:
            bool
        '''
        stack = deque()
        for i ,char in enumerate(expression): 
            if char == '(' or char == '[': 
                if i+1 >= len(expression) or expression[i+1] == ')' or expression[i+1] == ']':
                    return False
                stack.append(char)
            elif char == ')': 
                if len(stack) == 0 or stack.pop() != '(' : 
                    return False
               
            elif char == ']': 
                if len(stack) == 0 or stack.pop() != '[' : 
                    return False
               
        return len(stack) == 0
    
    def validate_no_neasted_square_brackets(self, expression:str) -> bool:
        '''
        This function validates the square brackets in the expression.
        It returns True if the square brackets are valid, otherwise it returns False.
        The square brackets are valid in the following case:
            1. no nested square brackets.

        Input:
            expression: str
        Output:
            bool
        ''' 
        stack = deque()
        for char in expression: 
            if char == '[': 
                if len(stack) != 0: # this mean that there is a nested square bracket.
                    return False
                stack.append(char)
            elif char == ']': 
                if len(stack) == 0 or stack.pop() != '[': 
                    return False
        return len(stack) == 0
    