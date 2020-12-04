# Solution to Session 9 Problem 5
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   November 3, 2020

input_file = open("rotamult-input.txt", "r")
output_file = open("rotamult-output.txt", "w")

while True:
    line = input_file.readline()

    if not line:
        break

    line = list(map(int, line.split()))

    # Algorithm per se
    base = line[0]
    lsd = line[1]
    multiplier = line[2]
    
    num_digits = 0

    product = lsd * multiplier
    carry = product // base
    next_digit = product % base
    num_digits += 1

    while not (next_digit == lsd and carry == 0):
        product = next_digit * multiplier + carry
        carry = product // base
        next_digit = product % base
        num_digits += 1

    output_file.write(str(num_digits) + "\n")

output_file.close()
input_file.close()
