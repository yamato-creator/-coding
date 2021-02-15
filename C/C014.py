s = input().split()
n = int(s[0])
r = int(s[1])

for i in range(n):
    t = input().split()
    h = int(t[0])
    w = int(t[1])
    d = int(t[2])
    if h >= r*2:
        if w >= r*2:
            if d >= r*2:
                print(i+1)
