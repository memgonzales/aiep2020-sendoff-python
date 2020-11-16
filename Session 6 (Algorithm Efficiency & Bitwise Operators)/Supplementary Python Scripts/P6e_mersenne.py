# Solution to Session 6 Problem 6e
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   September 3, 2020

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


def generate_mersenne_prime(num_mersenne_primes):
    list_mersenne = []

    # Treat 2^2 - 1 = 3 as a special case since 2 is the only prime number with the 
    # property that the number after it is also prime.
    
    list_mersenne.append(3)

    num_primes = 1
    candidate_exp = 3
    
    while num_primes < num_mersenne_primes:
        if is_prime(candidate_exp):
            # While it is possible to subtract 1 from a number using bitwise operators,
            # such an approach may be a bit contrived.
            candidate_mersenne = (1 << candidate_exp) - 1
            
            if is_prime(candidate_mersenne):
               list_mersenne.append(candidate_mersenne)
               num_primes = num_primes + 1

        # Skip even numbers.
        candidate_exp = candidate_exp + 2

    return list_mersenne


# Sample Run
print(generate_mersenne_prime(8))