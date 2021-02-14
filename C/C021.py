s = input().split()
xc = int(s[0])
yc = int(s[1])
r_1 = int(s[2])
r_2 = int(s[3])

n = int(input())

for i in range(n):
    xy = input().split()
    x = int(xy[0])
    y = int(xy[1])
    if r_1**2 <= (x-xc)**2 + (y-yc)**2 and r_2**2 >= (x-xc)**2 + (y-yc)**2:
        print("yes")
    else:
        print("no")