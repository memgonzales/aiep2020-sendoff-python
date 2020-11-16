# Solution to Session 6 Problem 10
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
#         Based on the original algorithmic description of Durstenfeld
#         (improvement over the Fisher-Yates shuffle)
# @date   September 12, 2020

import random

def shuffle_linear_time(array):
    for i in range(len(array) - 1, 1, -1):
        j = random.randint(0, i)

        # Perform swapping
        array[i], array[j] = array[j], array[i]

# Sample Runs
array = [1, 3, 5, 7, 9, 11, -13]
for i in range(5):
    shuffle_linear_time(array)
    print(array)