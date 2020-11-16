# Solution to Session 6 Problem 5
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   September 12, 2020

def largest_cont_product(array):
    largest_product = 1
    curr_max_product = 1
    curr_min_product = 1

    for i in range(len(array)):
        temp = curr_max_product
        
        # The caveat in the problem statement motivates the need for curr_min_product.
        curr_max_product = max(array[i], max(array[i] * curr_max_product,
                                        array[i] * curr_min_product))
        curr_min_product = min(array[i], min(array[i] * temp,
                                        array[i] * curr_min_product))
        largest_product = max(curr_max_product, largest_product)

    return largest_product

# Sample Runs
print(largest_cont_product([1, 2, 3]))
print(largest_cont_product([4, -5, -6, 8, -10, 0, 1, 8]))
print(largest_cont_product([-1, -2, 3, 0, -7, -8, -4, 4]))