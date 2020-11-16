# Solution to Session 7 Problem 4
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   October 16, 2020

class BinaryTreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
def num_leaves_bin_tree(root):
    if root is None:
        return 0

    if root.right is None and root.left is None:
        return 1
        
    return num_leaves_bin_tree(root.left) + num_leaves_bin_tree(root.right)
    
# Sample Run
root = BinaryTreeNode(3)
root.left = BinaryTreeNode(1)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.left.right.left = BinaryTreeNode(6)
root.right = BinaryTreeNode(7)
root.right.right = BinaryTreeNode(8)
root.right.right.right = BinaryTreeNode(2)
root.right.right.left = BinaryTreeNode(100)
root.right.right.left.right = BinaryTreeNode(200)

print(num_leaves_bin_tree(root))