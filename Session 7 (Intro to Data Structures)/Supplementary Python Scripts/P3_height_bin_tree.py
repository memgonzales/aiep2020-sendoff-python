# Solution to Session 7 Problem 3
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   October 15, 2020

class BinaryTreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
def height_bin_tree(root):
    if root is None:
        return -1

    left_height = height_bin_tree(root.left)
    right_height = height_bin_tree(root.right)
    
    return 1 + max(left_height, right_height)
    
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

print(height_bin_tree(root))
