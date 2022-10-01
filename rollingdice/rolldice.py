#!/usr/bin/python3
# A python program that simulates rolling of a dice 1000 times and accounts for the frequency of ecah face
# and the percentage of total dice rolls for each face

# import random
import random

# variable declarations
count = 0

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0


def getRandomNumberSum(num):
    global sum1, sum2, sum3, sum4, sum5, sum6
    if num >= 0/6 and num < 1/6:
        sum1 += 1
    elif num >= 1/6 and num < 2/6:
        sum2 += 1
    elif num >= 2/6 and num < 3/6:
        sum3 += 1
    elif num >= 3/6 and num < 4/6:
        sum4 += 1
    elif num >= 4/6 and num < 5/6:
        sum5 += 1
    elif num >= 5/6 and num < 6/6:
        sum6 += 1


# while count < 1000 program runs
while count < 1000:
    result = random.random()
    getRandomNumberSum(result)
    count += 1


# print table of values
print("|  side   |   frequency   |    percentage   |")
print("|---------|---------------|-----------------|")
array = [sum1, sum2, sum3, sum4, sum5, sum6]
totalsum = sum1 + sum2 + sum3 + sum4 + sum5 + sum6
totalpercentage = 0
for i in range(1, 7):
    percentage = round(((array[i-1]/totalsum) * 100), 1)
    totalpercentage += percentage
    print(f"|    {i}    |      {array[i-1]}      |      {percentage}%      |")
print("|---------|---------------|-----------------|")
print(
    f"|  total  |     {totalsum}      |      {round(totalpercentage)}%       |")
