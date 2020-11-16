# Solution to Session 7 Problem 9
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   October 22, 2020

MAX_HEIGHT_DIFFERENCE = 1

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

def is_height_balanced(root):
    if root is None:
        return True

    if abs(height_bin_tree(root.left) - height_bin_tree(root.right)) <= MAX_HEIGHT_DIFFERENCE \
       and is_height_balanced(root.left) and is_height_balanced(root.right):
        return True

    return False

# Sample Run
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(4)
root.left.right = BinaryTreeNode(5)
root.left.right.left = BinaryTreeNode(7)
root.right.right = BinaryTreeNode(6)

print(is_height_balanced(root))

root.left.right.left.right = BinaryTreeNode(6)
print(is_height_balanced(root))
