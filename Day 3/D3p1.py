from pathlib import Path 
import math

f = open("Day 3\\input.txt", "r")

sum = 0
prev = ""
lst = ["!","@","#","$","%","&","*","/","=","-","+"]
points = []
prevpoints = []
num = [1, []]
for x in f:
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
        
            
                
    for symbol in lst:
        newindex = 0
        for i in range(x.count(symbol)):
            newindex = x.find(symbol, newindex + 1)
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
    prev = x
print(sum)