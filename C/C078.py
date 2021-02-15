s = input().split()
N = int(s[0])
c_1 = int(s[1])
c_2 = int(s[2])
stocks = 0
profit = 0

for i in range(N):
    Stock_price = int(input())
    if c_1 >= Stock_price:
        stocks += 1
        profit = profit - Stock_price
    elif c_2 <= Stock_price:
        profit = profit + stocks * Stock_price
        stocks = 0

if stocks != 0:
    profit = profit + stocks * Stock_price
    stocks = 0
print(profit)
