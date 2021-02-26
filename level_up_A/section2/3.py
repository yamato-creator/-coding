y, x, d = input().split()

y = int(y)
x = int(x)

s = input()
if d == "N":
    if s == "R":
        x += 1
    elif s == "L":
        x -= 1
elif d == "W":
    if s == "R":
        y -= 1
    elif s == "L":
        y += 1
elif d == "S":
    if s == "R":
        x -= 1
    elif s == "L":
        x += 1
elif d == "E":
    if s == "R":
        y += 1
    elif s == "L":
        y -= 1

print(y,x)