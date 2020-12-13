# Solution to Session 10 Problem 11
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   November 4, 2020

import itertools
from itertools import permutations, chain

# Trial division with 6k plus/minus 1 optimization
def is_prime(num):
    if num <= 3:
        return num > 1
        
    if num % 2 == 0 or num % 3 == 0:
        return False
        
    cand_factor = 5
    
    while cand_factor * cand_factor <= num:
        if num % cand_factor == 0 or num % (cand_factor + 2) == 0:
            return False
            
        cand_factor = cand_factor + 6
        
    return True


def permute_powerset(array):
    return chain.from_iterable(permutations(array, r) for r in range(1, len(array) + 1))


input_file = open("spy-input.txt", "r")
output_file = open("spy-output.txt", "w")

input_file.readline()

while True:
    line = input_file.readline().rstrip()

    if not line:
        break
    
    # Algorithm per se
    digits = list(line)
    powerset_digits = set(permute_powerset(digits))
    
    # Convert permutations to integers
    prime_nums = set()
    
    for permute in powerset_digits:
        candidate_prime = int((''.join(map(str, permute))))
        if is_prime(candidate_prime):
            prime_nums.add(candidate_prime)

    output_file.write(str(len(prime_nums)) + "\n")
        
output_file.close()
input_file.close()
