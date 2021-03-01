N, R = map(int,input().split())
s = [int(input()) for _ in range(N)]
num = max(s) // R

for i in range(N):
    count = 0
    count = s[i] // R
    print(str(i + 1)+ ":" + count * "*" + (num-count) * ".")