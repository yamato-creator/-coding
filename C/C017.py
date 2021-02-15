s = input().split()
oya_a= int(s[0])
oya_b= int(s[1])
n = int(input())

for i in range(n):
    t = input().split()
    kodomo_a = int(t[0])
    kodomo_b = int(t[1])
    if oya_a == kodomo_a:
        if oya_b > kodomo_b:
            print("Low")
        elif oya_b < kodomo_b:
            print("High")
        elif oya_b == kodomo_b:
            print("Low")
    elif oya_a > kodomo_a:
        print("High")
    elif oya_a < kodomo_a:
        print("Low")