from pathlib import Path 
import math

f = open("Day 4\\input.txt", "r")

sum = 0
num = 0
for line in f:
    count = 0
    line = line.split("|")
    line[1] = line[1].split(" ")
    line[1][len(line[1]) - 1] = str(int(line[1][len(line[1]) - 1]))
    for number in line[0].split(" "):
        if number.find(":") == -1 and number.isdigit() and (number in line[1]):
            count += 1
    if count > 0:
        sum += pow(2, count - 1)
print(sum)