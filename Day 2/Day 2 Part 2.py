from pathlib import Path 


f = open("Day 2\\input.txt", "r")
prev = ""
sum = 0
for x in f:
    rgb = [0,0,0]
    x = x.split(" ")
    for s in x:
        prev.replace(":", "")
        if s.find("red") >= 0 and int(prev) > rgb[0]:
            rgb[0] = int(prev)
        elif s.find("blue") >= 0 and int(prev) > rgb[2]:
            rgb[2] = int(prev)
        elif s.find("green") >= 0 and int(prev) > rgb[1]:
            rgb[1] = int(prev)
        prev = s
    sum += (rgb[0] * rgb[1] * rgb[2])

print(sum)