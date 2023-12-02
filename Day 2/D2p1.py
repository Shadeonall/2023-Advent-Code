from pathlib import Path 


f = open("Day 2\\input.txt", "r")
prev = ""
sum = 0
for x in f:
    add = True
    x = x.split(" ")
    for s in x:
        prev.replace(":", "")
        if (s.find("red") >= 0 and int(prev) > 12) or (s.find("blue") >= 0 and int(prev) > 14) or (s.find("green") >= 0 and int(prev) > 13):
            add = False
            break
        prev = s
    if add:
        print(x[1].replace(":", ""))
        sum += int(x[1].replace(":", ""))

print(sum)