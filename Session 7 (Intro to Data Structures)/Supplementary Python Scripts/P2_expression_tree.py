# Solution to Session 7 Problem 2
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   October 22, 2020

class BinaryTreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def is_operator(token):
    operators = ['+', '-', '*', '/', '^']
    return token in operators

def construct_expression_tree(postfix):
    stack = []
    
    for token in postfix:
        if not is_operator(token):
            stack.append(BinaryTreeNode(token))
        else:
            operator = BinaryTreeNode(token)
            operator.right = stack.pop()
            operator.left = stack.pop()
            stack.append(operator)

    return stack.pop()                   

def print_prefix(expression_tree):
    if expression_tree:
        print(expression_tree.val, end = '')
        print_prefix(expression_tree.left)
        print_prefix(expression_tree.right)

# In reference to the caveat in the problem statement, the result should be
# an overly-parenthesized expression.
def print_infix(expression_tree):
    if expression_tree:
        if is_operator(expression_tree.val):
            print("(", end = '')
            
        print_infix(expression_tree.left)
        print(expression_tree.val, end = '')
        print_infix(expression_tree.right)
        
        if is_operator(expression_tree.val):
            print(")", end = '')

def print_postfix(expression_tree):
    if expression_tree:
        print_postfix(expression_tree.left)
        print_postfix(expression_tree.right)
        print(expression_tree.val, end = '')
        
    
# Sample Runs
expression_tree = construct_expression_tree("ab+ef*g*-")
print_prefix(expression_tree)
print()
print_infix(expression_tree)
print()
print_postfix(expression_tree)
