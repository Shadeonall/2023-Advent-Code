from pathlib import Path 
import math

f = open("Day 4\\input.txt", "r")

sum = 0
realNumber = 0
numCards = [1]*220
for line in f:
    count = 0
    line = line.split("|")
    line[1] = line[1].split(" ")
    line[1][len(line[1]) - 1] = str(int(line[1][len(line[1]) - 1]))
    for number in line[0].split(" "):
        if number.find(":") >= 0:
            number = number.replace(":", "")
            realNumber = int(number)
        elif number.isdigit() and (number in line[1]):
            count += 1
    for k in range(count):
        numCards[realNumber + k+1] += 1 * numCards[realNumber]
    sum += numCards[realNumber]
print(sum)