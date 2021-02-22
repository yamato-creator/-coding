s = input().split()
height = int(s[0])
width = int(s[1])
lst = []

for i in range(height):
    t = input().split()
    lst.append(t)
    for t in range(width):
        if int(lst[i][t]) <= 127:
            lst[i][t] = 0
        elif int(lst[i][t]) >= 128:
            lst[i][t] = 1
for i in range(height):
    s=' '.join(map(str,lst[i]))
    print(s)