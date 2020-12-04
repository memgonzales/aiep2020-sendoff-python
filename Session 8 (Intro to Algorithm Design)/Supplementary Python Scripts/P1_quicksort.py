# Solution to Session 8 Problem 1
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
#         Based on Hoare's algorithmic description
# @date   November 2, 2020

# Use Lomuto's partitioning scheme
def partition(array, start, end):
    pivot = array[end]
    less = start

    for i in range(start, end):
        if array[i] <= pivot:
            array[less], array[i] = array[i], array[less]
            less = less + 1
            
    array[less], array[end] = array[end], array[less]
    
    return less


def quicksort_helper(array, start, end):
    if start < end:
        index_pivot = partition(array, start, end)
        quicksort_helper(array, start, index_pivot - 1)
        quicksort_helper(array, index_pivot + 1, end)


def quicksort(array):
    quicksort_helper(array, 0, len(array) - 1)


# Sample Run
array = [-1, -5, -7, 2, 100, -4, 3, 0]
quicksort(array)
print(array)
