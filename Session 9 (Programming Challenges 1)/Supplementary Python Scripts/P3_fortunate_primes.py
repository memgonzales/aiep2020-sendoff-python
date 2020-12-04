# Solution to Session 9 Problem 3
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   November 3, 2020

# Primality testing using the 6k plus or minus 1 method
def is_prime(num):
    if num <= 3:
        return num > 1
    
    if num % 2 == 0 or num % 3 == 0:
        return False

    candidate_factor = 5
    while candidate_factor * candidate_factor <= num:
        if num % candidate_factor == 0 or num % (candidate_factor + 2) == 0:
            return False
        candidate_factor = candidate_factor + 6

    return True

def get_next_prime(num):
    while True:
        num = num + 1
        if is_prime(num):
            return num

def get_fortunate(primorial):
    m = 1
    while True:
        m = m + 1
        if is_prime(primorial + m):
            return m

def get_lesser_fortunate(primorial):
    m = 1
    while True:
        m = m + 1
        if is_prime(primorial - m):
            return m


fortunate_nums = set()

n = int(input())

num_fortunate = 0
primorial_factor = 2
primorial = 2

# First Fortunate number
fortunate_nums.add(3)

intersect_ctr = 0
while num_fortunate < n:
    primorial_factor = get_next_prime(primorial_factor)
    primorial = primorial * primorial_factor
    
    num_fortunate += 1

    if num_fortunate < n:
        fortunate_nums.add(get_fortunate(primorial))

    if get_lesser_fortunate(primorial) in fortunate_nums:
        intersect_ctr += 1

print(intersect_ctr)
