Winning_number = input().split()
N = int(input())

for i in range(N):
    numbers = input().split()
    judge = set(Winning_number) & set(numbers)
    print(len(judge))