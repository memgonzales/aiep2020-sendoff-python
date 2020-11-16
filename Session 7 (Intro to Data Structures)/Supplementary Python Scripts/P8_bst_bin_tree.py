# Solution to Session 7 Problem 8
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   October 21, 2020

import collections
from collections import deque

class BinaryTreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def bfs(root):
    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        print(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        
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

bfs(root)
