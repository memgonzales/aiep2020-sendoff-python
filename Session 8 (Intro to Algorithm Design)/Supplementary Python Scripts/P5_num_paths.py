# Solution to Session 8 Problem 5
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   November 2, 2020

import math

def num_paths_dp(m, n):
    table = [[1] * m for i in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            table[i][j] = table[i - 1][j] + table[i][j - 1]
            
    return table[n - 1][m - 1]

def num_paths_combi(m, n):
    return math.comb(m + n - 2, n - 1)


# Sample Runs
print(num_paths_dp(10, 5))
print(num_paths_combi(10, 5))

