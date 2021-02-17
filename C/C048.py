import math

s = input().split()
X = int(s[0])
P = int(s[1])

num = 0

s = 100 - P
ans = X
while math.floor(X) > 0:
    X = math.floor(X*s/100)
    ans += X
print(ans)