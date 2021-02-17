n = int(input())

variable_1 = 0
variable_2 = 0

for i in range(n):
    s = input().split()
    if s[0] == "SET":
        if int(s[1]) == 1:
            variable_1 = int(s[2])
        elif int(s[1]) == 2:
            variable_2 = int(s[2])
    elif s[0] == "ADD":
        variable_2 = variable_1 + int(s[1])
    elif s[0] == "SUB":
        variable_2 = variable_1 - int(s[1])
print(variable_1,variable_2)
