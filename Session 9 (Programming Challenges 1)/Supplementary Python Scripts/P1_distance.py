# Solution to Session 9 Problem 1
# 2020 AIEP Send-off
# @author Mark Edward M. Gonzales
# @date   November 3, 2020

num_features = int(input())
order_minkowski = int(input())

euclidean = 0
manhattan = 0
minkowski = 0

data_point1 = list(map(float, input().split()))
data_point2 = list(map(float, input().split()))

for feature1, feature2 in zip(data_point1, data_point2):
    difference = abs(feature1 - feature2)
    euclidean += difference ** 2
    manhattan += difference
    minkowski += difference ** order_minkowski

print("{:.6f}".format(round(euclidean ** 0.5, 6)))
print("{:.6f}".format(round(manhattan, 6)))
print("{:.6f}".format(round(minkowski ** (1 / order_minkowski), 6)))
