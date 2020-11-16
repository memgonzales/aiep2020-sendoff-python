# Solution to Session 6 Problem 4
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   September 12, 2020

def gmcc_largest_cont_sum(array):
    largest_sum = float('-inf')
    current_sum = 0

    for i in range(len(array)):
        current_sum = current_sum + array[i]
        if current_sum < array[i]:
            current_sum = array[i]
        if current_sum > largest_sum:
            largest_sum = current_sum

    return largest_sum

# Sample Runs
print(gmcc_largest_cont_sum([1, 2, 3]))
print(gmcc_largest_cont_sum([5, -6, 7, -2, 3, -5, 4]))
print(gmcc_largest_cont_sum([-1, -2, -3]))
print(gmcc_largest_cont_sum([-3, -2, -1]))