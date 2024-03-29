import re


ExpressionOpeners = ['(', '[', '{']
ExpressionClosers = [')', ']', '}']
Operators = ['+', '-', '*', '/', '^']
Delimiters = ExpressionOpeners + ExpressionClosers
Tokens = set(Operators + Delimiters)  # collection of Operators
Priority = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities of Operators
 
 
def infixToPostfix(infix: list): 

    # infix = parse_infix(infix)

    stack = [] # initialization of empty stack

    output = []

    for e in infix:

        if e not in Tokens:  # if an operand append in postfix expression

            output.append(e)

        elif e in ExpressionOpeners:  # else Operators push onto stack

            stack.append(e)

        elif e in ExpressionClosers:

            while stack and stack[-1] not in ExpressionOpeners: # as long as the stack is not empy and the '(' not not retrieved

                output.append(stack.pop())

            stack.pop() # pop the '(' out.

        else: 

            while stack and stack[-1] not in ExpressionOpeners and Priority[e]<=Priority[stack[-1]]:

                output.append(stack.pop())

            stack.append(e)

    while stack:
        output+=stack.pop()

    return output


def parse_infix(expr: str) -> list:
    """
        given an infix expression: -1 + 2 * 3/(4^5)-9
        generate ['0', '-', '1', '+', '2', '3', '/', '(', '4', '^', '5', ')', '-', '9'] 
        return : the last index of a number starting at start_index and ended at 'last_index'
    """
    
    infix = expr.replace(' ', '') # remove all white spaces, they are never useful

    better_infix = []

    val = ''
    for i in range(len(infix)):
        e = infix[i] 

        if e in ExpressionOpeners: 
            better_infix.append(e)

        elif e not in Tokens: # an operand: letter or digit
            val += e

        elif (e == '-' or e == '+') and (i == 0 or infix[i-1] in ExpressionOpeners):# initial '-' operator
            better_infix += ['0', '-']
    
        elif e in Tokens: # an symbol not a digit: 12+ or 12) or 12( etc...
            if val != '': better_infix += [val, e]
            else: better_infix.append(e)
            val = ''


    if val != '': better_infix.append(val) # last val won't have an op behind it so the 'else' statement won't work 

    print('INFIX: ', better_infix) 

    return better_infix