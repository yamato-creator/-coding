hate = int(input())
sickrooms = int(input())
k = 0
for i in range(sickrooms):
    s = input()
    if not str(hate) in s:
        print(int(s))
        k += 1
if k == 0:
    print("none")

