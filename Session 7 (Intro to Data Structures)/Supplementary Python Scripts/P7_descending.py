# Solution to Session 7 Problem 7
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   October 21, 2020

class BinaryTreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
		
def insert_bst(root, key):
    if root is None:
        root = BinaryTreeNode(key)
    elif root.val > key:
        root.left = insert_bst(root.left, key)
    elif root.val < key:
        root.right = insert_bst(root.right, key)
    
    return root

def print_descending(root):
    if root:
        print_descending(root.right)
        print(root.val)
        print_descending(root.left)
        
        
# Sample Run
root = BinaryTreeNode(8)
insert_bst(root, 3)
insert_bst(root, 10)
insert_bst(root, 1)
insert_bst(root, 6)
insert_bst(root, 14)
insert_bst(root, 4)
insert_bst(root, 7)
insert_bst(root, 13)

print_descending(root)
