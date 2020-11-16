# Solution to Session 7 Problem 1
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
#         Based on Dijkstra's shunting-yard algorithm
# @date   October 21, 2020

import collections
from collections import deque

UNKNOWN = -1

def incoming_priority(operator):
    priorities = {"+": 1,
                  "-": 1,
                  "*": 2,
                  "/": 2,
                  "^": 4,
                  "(": 100,
                  ")": 0}

    if operator in priorities.keys():
        return priorities[operator]
    else:
        return UNKNOWN


def instack_priority(operator):
    # The closing parenthesis is not pushed into the stack.
    priorities = {"+": 1,
                  "-": 1,
                  "*": 2,
                  "/": 2,
                  "^": 3,
                  "(": 0,}

    if operator in priorities.keys():
        return priorities[operator]
    else:
        return UNKNOWN

def is_operator(token):
    return incoming_priority(token) != UNKNOWN
                  
def infix_to_postfix(expression):
    postfix = deque()
    operators = []

    for token in expression:
        if not is_operator(token):
            postfix.append(token)
        else:
            while operators and incoming_priority(token) <= instack_priority(operators[-1]):
                temp = operators.pop()
                if temp == '(':
                    break
                else:
                    postfix.append(temp)

            if token != ')':
                operators.append(token)

    while operators:
        postfix.append(operators.pop())                

    return postfix


# Sample Runs
print(infix_to_postfix("2^3^4"))
print(infix_to_postfix("1*2+3"))
print(infix_to_postfix("1+2*3"))
print(infix_to_postfix("(1+2)*3"))
print(infix_to_postfix("3/3+2*3-1"))
print(infix_to_postfix("3/3+2*(3-1)"))
print(infix_to_postfix("3/(3+2)*3-1"))
    

