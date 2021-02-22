cards = list(map(int, input().split()))
max_1 = max(cards)
cards.remove(max_1)
max_2 = max(cards)
cards.remove(max_2)

result = 10 * max_1 + 10 * max_2 + sum(cards)
print(result)