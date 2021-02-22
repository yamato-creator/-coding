s = input().split()
row = int(s[0])
column = int(s[1])
lst = []
result = []
result_AB = []
for i in range(row):
    t = list(map(int, input().split()))
    lst.append(t)

for i in lst:
    count = 0
    divide = sum(i) // 2
    for t in range(column):
        tmp = i[t]
        count = count + tmp
        if count == divide:
            result.append("Yes")
            result_AB.append(str("A" * (t+1)) + str("B" * (5-(t + 1)))) 
            break

if len(result) == row:
    print("Yes")
    for i in result_AB:
        print(i)
else:
    print("No")
