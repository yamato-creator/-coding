x, y, n = map(int, input().split())
d = "N"

for i in range(n):
    s = input()
    if d == "N":
        if s == "L":
            x -= 1
            d = "W"
            print(x, y)
        elif s == "R":
            x += 1
            d = "E"
            print(x, y)
    elif d == "W":
        if s == "L":
            y += 1
            d = "S"
            print(x, y)
        elif s == "R":
            y -= 1
            d = "N"
            print(x, y)
    elif d == "S":
        if s == "L":
            x += 1
            d = "E"
            print(x, y)
        elif s == "R":
            x -= 1
            d = "W"
            print(x, y)
    elif d == "E":
        if s == "L":
            y -= 1
            d = "N"
            print(x, y)
        elif s == "R":
            y += 1
            d = "S"
            print(x, y)