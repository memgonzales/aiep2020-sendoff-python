# Solution to Session 8 Problem 6
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   November 2, 2020

class BinaryTreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def sum_odd_parents_helper(root, parent_val):
    if root:
        if parent_val % 2 != 0:
            return root.val + sum_odd_parents_helper(root.left, root.val) + sum_odd_parents_helper(root.right, root.val)
        else:
            return sum_odd_parents_helper(root.left, root.val) + sum_odd_parents_helper(root.right, root.val)

    return 0

def sum_odd_parents(root):
    # Any even number will suffice as being the key stored in the "parent" of the root.
    return sum_odd_parents_helper(root, 0)


# Sample Run
root = BinaryTreeNode(8)
root.left = BinaryTreeNode(3)
root.right = BinaryTreeNode(10)
root.left.left = BinaryTreeNode(1)
root.left.right = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(14)
root.left.right.left = BinaryTreeNode(4)
root.left.right.right = BinaryTreeNode(7)
root.right.right.left = BinaryTreeNode(13)

print(sum_odd_parents(root))   
