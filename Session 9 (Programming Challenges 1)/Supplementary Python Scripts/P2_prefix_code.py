# Solution to Session 9 Problem 2
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   November 3, 2020

class BinaryTreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def construct_prefix_tree():
    root = BinaryTreeNode('\0')
    root.left = BinaryTreeNode('A')
    root.right = BinaryTreeNode('\0')
    root.right.left = BinaryTreeNode('\0')
    root.right.left.left = BinaryTreeNode('E')
    root.right.left.right = BinaryTreeNode('O')
    root.right.right = BinaryTreeNode('\0')
    root.right.right.left = BinaryTreeNode('\0')
    root.right.right.right = BinaryTreeNode('\0')
    root.right.right.right.left = BinaryTreeNode('S')
    root.right.right.left.left = BinaryTreeNode('U')
    root.right.right.left.right = BinaryTreeNode('\0')
    root.right.right.right.right = BinaryTreeNode('\0')
    root.right.right.left.right.right = BinaryTreeNode('D')
    root.right.right.right.right.right = BinaryTreeNode('G')
    root.right.right.left.right.left = BinaryTreeNode('K')
    root.right.right.right.right.left = BinaryTreeNode('B')
    
    return root


root = construct_prefix_tree()
num_test_cases = int(input())

decoded_strings = []

for _ in range(num_test_cases):
    encoded = input()
    decoded = ""

    i = 0
    while i < len(encoded):
        curr = root

        while curr:
            prev = curr

            if i < len(encoded):
                if encoded[i] == '1':
                    curr = curr.right
                else:
                    curr = curr.left
            else:
                break

            i += 1

        decoded += prev.val
        
        if i == len(encoded):
            break
        
        i -= 1

    if decoded == '\0':
        decoded = "BAMBOOZLED"

    decoded_strings.append(decoded)

for decoded in decoded_strings:
    print(decoded)      
