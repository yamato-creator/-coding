n = int(input())
k = 0
s = 0
e = 0
h = 0
l = 1000000

for i in range(n):
    k += 1
    x = input().split()
    if int(x[2]) > h:
        h = int(x[2])
    if int(x[3]) < l:
        l = int(x[3])
    if k == 1:
        s = x[0]
    if k == n:
        e = x[1]

print(s,e,h,l)