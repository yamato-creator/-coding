import math

s = input().split()
k = int(s[0])
n = int(s[1])

for i in range(k):
    t = input().split()
    score = math.floor(int(t[1]) * 100 / n)
    if 1 <= int(t[0]) and int(t[0]) <= 9:
        score = math.floor(score * 0.8)
    elif int(t[0]) > 9:
        score = 0
    if score >= 80:
        print("A")
    elif score <= 79 and score >= 70:
        print("B")
    elif score <= 69 and score >= 60:
        print("C")
    elif score <= 59 and score >= 0:
        print("D")