# Solution to Session 6 Problem 8
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   September 12, 2020

# b. O(n^2)
# c. Traverses the list too many times, does not take advantage
#    of "information" from previously scanned values
# d. No, regardless of the order of the data values in the input,
#    the number of steps does not change since it will still need to
#    traverse the entire unsorted sublist to get the minimum.

def selection_sort(array):
    for i in range(len(array) - 1):
        minIndex = i

        # Scan the unsorted sublist to get the minimum
        for j in range(i + 1, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j

        # Swap the pertinent values
        temp = array[minIndex]
        array[minIndex] = array[i]
        array[i] = temp
        
    
# Sample Run
array = [-1, -5, -7, 2, 100, -4, 3, 0]
selection_sort(array)
print(array)