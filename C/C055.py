N = int(input())
G = input()
k = 0

for i in range(N):
    s = input()
    if G in s:
        print(s)
        k += 1

if k == 0:
    print("None")