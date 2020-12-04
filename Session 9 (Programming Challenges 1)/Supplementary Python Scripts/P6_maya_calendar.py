# Solution to Session 9 Problem 6
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   November 3, 2020

input_file = open("maya-input.txt", "r")
output_file = open("maya-output.txt", "w")

haab = ["pop", "no", "zip", "zotz", "tzec", "xul", "yoxkin", "mol", "chen", 
        "yax", "zac", "ceh", "mac", "kankin", "muan", "pax", "koyab", "cumhu", "uayet"]
tzolkin = ["imix", "ik", "akbal", "kan", "chicchan", "cimi", "manik", "lamat", "muluk", 
           "ok", "chuen", "eb", "ben", "ix", "mem", "cib", "caban", "eznab", "canac", "ahau"]

output_file.write(input_file.readline())

while True:
    line = input_file.readline()

    if not line:
        break

    line = line.split()

    # Algorithm per se
    day = int(line[0][:-1])
    month = line[1]
    year = int(line[2])

    total_days = year * 365 + haab.index(month) * 20 + day
    tzolkin_number = total_days % 13 + 1
    tzolkin_day = total_days % len(tzolkin)
    tzolkin_year = total_days // 260

    output_file.write(str(tzolkin_number) + " " + tzolkin[tzolkin_day] + " " + str(tzolkin_year) + "\n")

output_file.close()
input_file.close()
