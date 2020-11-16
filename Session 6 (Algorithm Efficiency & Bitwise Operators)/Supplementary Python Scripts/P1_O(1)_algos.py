# Solution to Session 6 Problem 1
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   September 3, 2020

def sum_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

def sum_cubes(n):
    return (n * (n + 1) // 2) ** 2

def max_intersect(n):
    return (n - 1) * n // 2

def num_diagonals(n):
    return n * (n -3) // 2

# Sample Runs
n = 100

print(sum_squares(n))
print(sum_cubes(n))
print(max_intersect(n))
print(num_diagonals(n))