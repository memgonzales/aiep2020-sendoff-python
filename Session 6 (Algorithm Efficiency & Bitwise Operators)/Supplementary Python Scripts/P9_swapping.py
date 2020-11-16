# Solution to Session 6 Problem 9
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   September 12, 2020

def swap_freestyle(a, b):
    c = a
    a = b
    b = c

    return [a, b]

def swap_two_variables(a, b):
    a = a + b
    b = a - b
    a = a - b

    return [a, b]

def swap_bitwise(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b

    return [a, b]

# Sample Runs
print(swap_freestyle(-5, 2))
print(swap_two_variables(-5, 2))
print(swap_bitwise(-5, 2))