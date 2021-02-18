Q = int(input())
k = 1
total = 0

for i in range(Q):
    N = int(input())
    while not k == N:
        if N % k == 0:
            total = total + k
        k += 1
    if total == N:
        print("perfect")
        k =1
        total = 0
    elif total == N-1:
        print("nearly")
        k =1
        total = 0
    else:
        print("neither")
        k =1
        total = 0