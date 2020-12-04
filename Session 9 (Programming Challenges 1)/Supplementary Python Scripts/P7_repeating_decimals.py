# Solution to Session 9 Problem 7
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   November 3, 2020

input_file = open("decimals-input.txt", "r")
output_file = open("decimals-output.txt", "w")

while True:
    line = input_file.readline()

    if not line:
        break

    line = list(map(int, line.split()))
    numerator = line[0]
    denominator = line[1]

    # Algorithm per se
    before_dec = ""
    after_dec = ""
    after_dec_paren = ""
    modulos_indices = {}

    before_dec = str(numerator // denominator)
    modulo_with_zero = numerator % denominator * 10

    index = 0
    while modulo_with_zero not in modulos_indices.keys():
        modulos_indices[modulo_with_zero] = index
        after_dec += str(modulo_with_zero // denominator)
        modulo_with_zero = modulo_with_zero % denominator * 10
        
        index = index + 1

    cycle_length = index - modulos_indices[modulo_with_zero]

    after_dec_paren = after_dec[0:modulos_indices[modulo_with_zero]] + "("
    if cycle_length <= 50:
        after_dec_paren += after_dec[modulos_indices[modulo_with_zero]:]
    else:
        after_dec_paren += after_dec[modulos_indices[modulo_with_zero]:modulos_indices[modulo_with_zero] + 50] + "..."
    after_dec_paren += ")"
        
    output_file.write(str(numerator) + "/" + str(denominator) + " = " + before_dec + "." + after_dec_paren + "\n" + \
                      "   " + str(cycle_length) + " = number of digits in repeating cycle\n\n")

output_file.close()
input_file.close()
