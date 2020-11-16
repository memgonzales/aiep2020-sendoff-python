# Solution to Session 6 Problem 3
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   September 12, 2020

def floor_sqrt_binary(n):    
    left = 1
    right = n

    while left <= right:
        mid = (left + right) // 2
        square_mid = mid * mid

        if square_mid == n:
            return mid
        elif square_mid < n:
            left = mid + 1
            # We are interested in the floor function
            result = mid
        else:
            right = mid - 1

    return result

# Sample Runs
print(floor_sqrt_binary(121))
print(floor_sqrt_binary(45))
print(floor_sqrt_binary(2))
print(floor_sqrt_binary(1))