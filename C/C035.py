N = int(input())
num = 0

for i in range(N):
    s = input().split()
    total = int(s[1])+int(s[2])+int(s[3])+int(s[4])+int(s[5])
    if total >= 350:
        if s[0] == "s":
            s_total = int(s[2])+int(s[3])
            if s_total >= 160:
                num += 1
        if s[0] == "l":
            l_total = int(s[4])+int(s[5])
            if l_total >= 160:
                num += 1
print(num)