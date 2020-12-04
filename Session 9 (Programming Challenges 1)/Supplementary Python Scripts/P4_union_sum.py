# Solution to Session 9 Problem 4
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   November 3, 2020

# O(1) solution
# Makes use of the method of finite differences to generate a closed-form expression
# for the union sum (which turns out to be a cubic polynomial)
def union_sum(num):
    x = (num - 1) // 2

    # Add 0.000000001 to circumvent floating-point error
    return int(16/3 * x**3 + 10 * x**2 + 26/3 * x + 1 + 0.000000001)

print(union_sum(int(input())))
