s = input().split()
N = int(s[0])
X = int(s[1])
bin_X = bin(X)
for i in range(N):
    t = int(input())
    print(bin_X[len(bin_X)-t])