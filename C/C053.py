N = int(input())

cards = input().split()
bonus = 1

if "x10" in cards:
    cards.remove("x10")
    bonus = 10

cards = [int(s) for s in cards]

if 0 in cards:
    max_card = max(cards)
    cards.remove(max_card)

result =sum(cards) * bonus

print(result)