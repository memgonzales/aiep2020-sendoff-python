# Solution to Session 6 Problem 2
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   September 4, 2020

# Recursive implementation of the Euclidean algorithm
def euclidean_gcd(a, b):
    if b == 0:
        return a 
    else:
        return euclidean_gcd(b, a % b)
        
# Sample Runs
print(euclidean_gcd(24, 32))
print(euclidean_gcd(32, 24))
print(euclidean_gcd(24, 101))
print(euclidean_gcd(101, 24))