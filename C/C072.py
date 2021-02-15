Ability_score = input().split()
attack = int(Ability_score[0])
defense = int(Ability_score[1])
agility = int(Ability_score[2])

N = int(input())
k = 0
for i in range(N):
    s = input().split()
    if int(s[1])<= attack and attack <= int(s[2]):
        if int(s[3])<= defense and defense <= int(s[4]):
            if int(s[5])<= agility and agility <= int(s[6]):
                print(s[0])
                k +=1
if k == 0:
    print("no evolution")