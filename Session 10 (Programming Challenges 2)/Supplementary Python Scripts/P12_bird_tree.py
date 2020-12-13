# Solution to Session 10 Problem 12
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
#         Based on the properties described by Hinze (2009)
# @date   November 4, 2020

input_file = open("bird-input.txt", "r")
output_file = open("bird-output.txt", "w")

input_file.readline()

while True:
    line = input_file.readline()

    if not line:
        break
    
    virgule = line.find("/")
    numerator = int(line[:virgule])
    denominator = int(line[virgule + 1:])

    path = ""
    while numerator != denominator:
        difference = numerator - denominator

        if difference > 0:
            path += "R"
            numerator, denominator = denominator, difference

        else:
            path += "L"
            numerator, denominator = -1 * difference, numerator

    output_file.write(path + "\n")

output_file.close()
input_file.close()
