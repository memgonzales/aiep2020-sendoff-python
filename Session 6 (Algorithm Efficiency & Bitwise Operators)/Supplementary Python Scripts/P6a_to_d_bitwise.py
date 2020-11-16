# Solution to Session 6 Problem 6a to d
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   September 3, 2020

def to_lowercase(ch):
    return chr(ord(ch) | 32)

def is_power_of_2(num):
    if num == 0:
        return False
    else:
        return not(num & (num - 1))

def divide_power_of_2(num, exp):
    return num >> exp

def multiply_power_of_2(num, exp):
    return num << exp

# Sample Runs
print(to_lowercase('D'))
print(is_power_of_2(0))
print(is_power_of_2(2048))
print(is_power_of_2(2049))
print(divide_power_of_2(1000, 3))
print(multiply_power_of_2(1000, 3))