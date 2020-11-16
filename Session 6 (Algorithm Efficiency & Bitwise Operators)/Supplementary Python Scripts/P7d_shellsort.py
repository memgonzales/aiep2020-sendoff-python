# Solution to Session 6 Problem 7d
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
#         Based on the original algorithmic description of Shell
#         (using Hibbard's increments)
# @date   October 15, 2020

def shellsort(array):
    # Use Hibbard's gap sequence: 1, 3, 7, 15, 31, ..., 2^k - 1.
    # Compute for the largest possible gap that array can admit.
    gap = 1
    while gap < len(array) // 2:
        gap = gap * 2 + 1
    
    while gap >= 1:
        # h-sort the set of values using insertion sort.
        for i in range(gap, len(array)):
            element = array[i]
            j = i
            while j > 0 and array[j - gap] > element:
                array[j] = array[j - gap]
                j = j - gap
            array[j] = element
            
        gap = gap // 2


# Sample Run
array = [-1, -5, -7, 2, 100, -4, 3, 0]
shellsort(array)
print(array)            