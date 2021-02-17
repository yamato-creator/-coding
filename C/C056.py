s = input().split()
N = int(s[0])
M = int(s[1])

if M == 0:
    for i in range(N):
        print(i+1)
else:
    for i in range(N):
        t = input().split()
        score = int(t[0])
        num = int(t[1])
        if not num == 0:
            score = score - num * 5
        if M <= score:
            print(i + 1)