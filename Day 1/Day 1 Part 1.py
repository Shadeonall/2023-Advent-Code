from pathlib import Path 


f = open("Day 1\input.txt", "r")
sum = 0
for x in f:
    x = ''.join(k for k in x if k.isdigit())
    sum += int(x[0]) * 10 + int(x[len(x) - 1])
    
print(sum)