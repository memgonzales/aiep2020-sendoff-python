# Solution to Session 10 Problem 8
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   November 3, 2020

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


def find_mersenne_prime(lower_bound):
    if lower_bound <= 3:
        return 3
    
    candidate_exp = 3
    
    while True:
        if is_prime(candidate_exp):
            # While it is possible to subtract 1 from a number using bitwise operators,
            # such an approach may be a bit contrived.
            candidate_mersenne = (1 << candidate_exp) - 1
            
            if is_prime(candidate_mersenne) and candidate_mersenne > lower_bound:
               return (candidate_mersenne, candidate_exp)

        # Skip even numbers.
        candidate_exp = candidate_exp + 2


# Follows the Carter-Wegman trick presented by M.A. Weiss (2014)
def fast_universal_hash(x, a, b, M):
    # To satisfy restriction a
    mersenne = find_mersenne_prime(M)

    # To satisfy restriction b
    hash_val = a * x + b
    hash_val = ((hash_val >> mersenne[1]) + (hash_val & mersenne[0]))
    if hash_val >= mersenne[0]:
        hash_val = hash_val - mersenne[0]

    # To satisfy restriction c
    return hash_val % M

x = int(input())
a = int(input())
b = int(input())
M = int(input())

print(fast_universal_hash(x, a, b, M))
