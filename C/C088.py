N = int(input())
s = list(map(int,input().split()))
money, num = map(int,input().split())

for i in range(num):
    number, quantity= map(int,input().split())
    if money >= quantity * s[number-1]:
        money = money - quantity * s[number-1]
print(money)