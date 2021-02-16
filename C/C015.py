import math

n = int(input())
point = 0

for i in range(n):
    s = input().split()
    d = s[0]
    p = int(s[1])
    if str(3) in d:
        point = point + math.floor(p * 0.03)
    elif str(5) in d:
        point = point + math.floor(p * 0.05)
    else:
        point = point + math.floor(p * 0.01)
print(point)