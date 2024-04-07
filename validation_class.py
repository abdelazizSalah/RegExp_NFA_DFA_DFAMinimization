from collections import deque

class Validation: 
    def __init__(self): 
        print('calling validation')
        self.special_char = {char: 1 for char in ['+', '|', '?', '*','-']}
        self.alphanumeric_char = {char: 1 for char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.'}
        self.paranteses = {char: 1 for char in ['(', ')', '[', ']']}

    def empty_expression(self,expression): 
        '''
            this returns true if the given expression is empty.
        '''
        return len(expression) == 0
    
    def valid_starting_char(self,expression):
        '''
            this returns false, if the expression starts with special characters, or any undefined characters. 
        '''
        return (expression[0] in self.paranteses) or ( expression[0] in self.alphanumeric_char)

    def no_sequence_of_special_char(self,expression):
        '''
            this returns false if there is any sequence of special characters such as 
                **
                ??
                +++
        
        '''
        # [[]] handeled in valid parantheses
        # (()) allowed
        valid=False
        for char in expression:
            if char in self.special_char :
                if valid:
                    return False
                valid = True
            else:    
                valid = False
        return True        

    def no_end_with_dash_or_pip(self, expression):
        '''
            this returns true if the expression doesn't end with '-' or '|'
        '''
        if expression[-1] == '-' or expression[-1] == '|':  #new
            return False
        for i,char in enumerate(expression):
            if char == ']' or char == ')':
                if expression[i-1] == '-' or expression[i-1] == '|':
                    return False
            if char == '[' or char == '(':
                if expression[i+1] == '-' or expression[i+1] == '|':
                    return False
        return True
    
    def no_special_char_in_parantheses(self, expression):
        '''
            this return true if there is no special character inside the parantheses.
        '''
        rounded_brackets=False
        new_special_char = {char: 1 for char in ['+', '|', '?', '*']}
        paranthes=False
        prev_paranthes=False
        for i,char in enumerate(expression):
            if rounded_brackets and char == '-': 
                return False
            if char == '[':
                prev_paranthes = True
                paranthes = True
            if char == ']':
                paranthes = False
                prev_paranthes = False
            if paranthes and char in new_special_char:
                return False
            
            # check () doesn't start with special char      #new
            if char == '(':
                paranthes=False
                rounded_brackets = True
                if(expression[i+1] in self.special_char):
                    return False
            if char == ')':
                rounded_brackets = False
                paranthes=prev_paranthes

        return True

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
    
    def validate_regular_expression(self, expression: str) -> bool: 
        ''' 
            This is the main validation function, which calls all the above utility validation functions. 

            Sequence of validation:
                1. empty
                2. valid starting character
                3. parentheses 
                    3.1. no empty parentheses and valid parentheses.
                    3.2. no nested square brackets
                4. no special characters inside the parentheses. 
                5. no sequence of special characters
                6. no end with dash or pipe
                 


        '''
        if self.empty_expression(expression): 
            return False
        
        if not self.valid_starting_char(expression):
            return False
        
        if not self.validate_parentheses(expression):
            return False
        
        if not self.validate_no_neasted_square_brackets(expression):
            return False
        
        if not self.no_special_char_in_parantheses(expression):
            return False
        
        if not self.no_sequence_of_special_char(expression):
            return False
        
        if not self.no_end_with_dash_or_pip(expression): 
            return False
        
        # it passed all tests.
        print("Passed all test cases 🥂🥳")
        return True
        
        
