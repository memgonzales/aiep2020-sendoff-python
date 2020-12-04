# Solution to Session 8 Problem 4
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   November 2, 2020

def tribonacci_top_down(n):
    memoization_table = {}
    memoization_table[1] = 0
    memoization_table[2] = 0
    memoization_table[3] = 1

    if n in memoization_table.keys():
        return memoization_table[n]
    else:
        nth_term = tribonacci_top_down(n - 1) + tribonacci_top_down(n - 2) + tribonacci_top_down(n - 3)
        memoization_table[n] = nth_term
        return nth_term

def tribonacci_bottom_up(n):
    t1 = 0
    t2 = 0
    t3 = 1

    if n == 1:
        return t1
    elif n == 2:
        return t2
    elif n == 3:
        return t3


    for i in range(4, n + 1):
        t3 = t1 + t2 + t3
        t2 = t3 - t2 - t1
        t1 = t3 - t2 - t1

    return t3

# Sample Runs
for i in range(1, 21):
    print(tribonacci_top_down(i))
    print(tribonacci_bottom_up(i))
