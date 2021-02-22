N = int(input())
mn = 200
mx = 0

for i in range(N):
    s = input().split()
    which = s[0]
    height = float(s[1])
    if s[0] == "ge":
        if height >= mx:
            mx = height
    elif s[0] == "le":
        if height <= mn:
            mn = height
print(mx,mn)