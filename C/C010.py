s = input().split()

a = int(s[0])
b = int(s[1])
R = int(s[2])

N = int(input())

for i in range(N):
    t = input().split()
    x = int(t[0])
    y = int(t[1])
    if (x-a)**2 + (y-b)**2 >= R**2:
        print("silent")
    else:
        print("noisy")