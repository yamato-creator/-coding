N, velocity = map(int,input().split())
result = "NO"
s = [list(input().split()) for _ in range(N)]
# print(s)

for i in range(len(s)):
    if int(s[i][0]) == 0 or int(s[i][1]) == 0:
        continue
    elif velocity <= (int(s[i][0]) / int(s[i][1])):
        result = "YES"

print(result)