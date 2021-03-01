before, operator, after, equal, answer = input().split()
if before == "x":
    if operator == "+":
        print(int(answer) - int(after))
    elif operator == "-":
        print(int(answer) + int(after))
elif after == "x":
    if operator == "+":
        print(int(answer) - int(before))
    elif operator == "-":
        print(int(before) - int(answer))
elif answer == "x":
    if operator == "+":
        print(int(before) + int(after))
    elif operator == "-":
        print(int(before) - int(after))