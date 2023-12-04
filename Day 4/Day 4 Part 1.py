from pathlib import Path 
import math

f = open("Day 4\\input.txt", "r")

sum = 0
num = 0
for x in f:
    count = 0
    x = x.split("|")
    x[1] = x[1].split(" ")
    x[1][len(x[1]) - 1] = str(int(x[1][len(x[1]) - 1]))
    for y in x[0].split(" "):
        if y.find(":") == -1 and y.isdigit() and (y in x[1]):
            count += 1
    if count > 0:
        sum += pow(2, count - 1)
print(sum)