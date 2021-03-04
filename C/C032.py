import math

N = int(input())

foods = 0
books = 0
clothes = 0
others = 0

for i in range(N):
    s = list(map(int, input().split()))
    if s[0] == 0:
        foods = foods + s[1]
    elif s[0] == 1:
        books = books + s[1]
    elif s[0] == 2:
        clothes = clothes + s[1]
    elif s[0] == 3:
        others = others  + s[1]

total_points = math.floor(foods / 100) * 5 + math.floor(books / 100) * 3 + math.floor(clothes / 100) * 2 + math.floor(others / 100) * 1

print(total_points)