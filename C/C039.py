s = input()
l = s.split("+")

i = 0
total = 0
while i < len(l):
    syounari = l[i].count("<")
    surassyu = l[i].count("/")
    total = total + 10 * syounari + 1 * surassyu
    i += 1

print(total)