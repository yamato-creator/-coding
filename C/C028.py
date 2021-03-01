N = int(input())
s = [list(input().split()) for _ in range(N)]
result = 0

for spell in s:
    if len(spell[0]) == len(spell[1]):
        answer = list(spell[0])
        my_answer = list(spell[1])
        count = 0
        for i in range(len(answer)):
            if answer[i] !=  my_answer[i]:
                count += 1
        if count == 0:
            result = result + 2
        elif count == 1:
            result = result + 1
        else:
            result = result + 0
print(result)