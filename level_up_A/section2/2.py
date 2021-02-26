y, x, n= map(int, input().split())

for i in range(n):
    s = input()
    if s == "N":
        y = y - 1
        print(y,x)
    elif s == "W":
        x = x - 1
        print(y,x)
    elif s == "S":
        y = y + 1
        print(y,x)
    elif s == "E":
        x = x + 1
        print(y,x)