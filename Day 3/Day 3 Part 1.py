from pathlib import Path 
import math

f = open("Day 3\\input.txt", "r")

sum = 0
prev = ""
lst = ["!","@","#","$","%","&","*","/","=","-","+"]
points = []
prevpoints = []
num = [1, []]
for line in f:
    prevletter = []
    points = []
    for letter in range(len(line)):
        if not line[letter].isdigit() and line[letter-1].isdigit():
            num = [0,[]]
            for value in range(len(prevletter)):
                num[0] = int(pow(10, value)) * int(prevletter[value][0]) + num[0]
                num[1].append(prevletter[value][1])
            prevletter = []  
            points.append(num)
        elif line[letter].isdigit():
            prevletter.insert(0, [line[letter], letter])
        
            
                
    for symbol in lst:
        newindex = 0
        for i in range(line.count(symbol)):
            newindex = line.find(symbol, newindex + 1)
            for k in prevpoints:
                if newindex in k[1] or (newindex + 1) in k[1] or (newindex - 1) in k[1]:
                    sum += k[0]
                    continue
            for k in points:
                if newindex in k[1] or (newindex + 1) in k[1] or (newindex - 1) in k[1]:
                    sum += k[0]
                    continue
        newindex = 0
        for i in range(prev.count(symbol)):
            newindex = prev.find(symbol, newindex + 1)
            for k in points:
                if newindex in k[1] or (newindex + 1) in k[1] or (newindex - 1) in k[1]:
                    sum += k[0]
                    continue
            
                    
    prevpoints = points        
    prev = line
print(sum)