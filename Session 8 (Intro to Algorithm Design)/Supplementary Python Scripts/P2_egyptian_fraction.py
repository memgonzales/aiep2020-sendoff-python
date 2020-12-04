# Solution to Session 8 Problem 2
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   November 2, 2020

import math

def egyptian_fraction(numerator, denominator):
    egyptian = []

    while numerator != 0:
        unit_denom = math.ceil(denominator / numerator)
        egyptian.append("1/" + str(unit_denom))
        denominator = unit_denom * denominator
        numerator = numerator * unit_denom - denominator // unit_denom
        
    return egyptian

# Sample Runs
print(egyptian_fraction(6, 13))
print(egyptian_fraction(31, 101))
