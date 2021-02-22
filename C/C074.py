import math

s = list(map(int, input().split()))
row = s[0]
column = s[1]
change_column = s[2]
count = 0

lst = [input() for i in range(row)]

t = math.ceil(row * column / change_column)
tmp = ''.join(lst)
for i in range(t):
    if len(tmp) < change_column:
        print(tmp)
    else:
        print(tmp[:change_column])
        tmp = tmp[change_column:]