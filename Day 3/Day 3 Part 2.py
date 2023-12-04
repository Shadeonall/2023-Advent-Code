from pathlib import Path 
import math

f = open("Day 3\\input.txt", "r")
line = f.readlines()
sum = 0
prev, curr, next = "", "", ""
symbol = "*"
points = []
prevpoints = []
num = [1, []]
count = [0]


def getNumbers(x):
    prevletter = []
    points = []
    for letter in range(len(x)):
        if not x[letter].isdigit() and x[letter-1].isdigit():
            num = [0,[]]
            for value in range(len(prevletter)):
                num[0] = int(pow(10, value)) * int(prevletter[value][0]) + num[0]
                num[1].append(prevletter[value][1])
            prevletter = []  
            points.append(num)
        elif x[letter].isdigit():
            prevletter.insert(0, [x[letter], letter])
    return points


for x in range(len(line)):
    curr = getNumbers(line[x])
    if(x != len(line) - 1):
        next = getNumbers(line[x+1])
    newindex = 0
    for i in range(line[x].count(symbol)):
        newindex = line[x].find(symbol, newindex + 1)
        for k in prev:
            if newindex in k[1] or (newindex + 1) in k[1] or (newindex - 1) in k[1]:
                count[0] += 1
                count.append(k[0])                    
                continue
        for k in curr:
            if newindex in k[1] or (newindex + 1) in k[1] or (newindex - 1) in k[1]:
                count[0] += 1
                count.append(k[0])                    
                continue
        for k in next:
            if newindex in k[1] or (newindex + 1) in k[1] or (newindex - 1) in k[1]:
                count[0] += 1
                count.append(k[0])                   
                continue
        if(count[0] == 2):
            sum += count[1] * count[2]
        count = [0]
    prev = getNumbers(line[x])
    
print(sum)