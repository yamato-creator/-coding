H, W, sy, sx, N = map(int,input().split())
d = "N"
s = [list(input()) for _ in range(H)]

for i in range(N):
    m = input()
    if d == "N":
        if m == "L":
            sx -= 1
            if sx >= 0 and s[sy][sx] == ".":
                d = "W"
                print(sy, sx)
            else:
                print("Stop")
                break
        elif m =="R":
            sx += 1
            if sx < W + 1  and s[sy][sx] == ".":
                d = "E"
                print(sy, sx)
            else:
                print("Stop")
                break
    elif d == "W":
        if m == "L":
            sy += 1
            if sy < H + 1 and s[sy][sx] == ".":
                d = "S"
                print(sy, sx)
            else:
                print("Stop")
                break
        elif m =="R":
            sy -= 1
            if sy >= 0  and s[sy][sx] == ".":
                d = "N"
                print(sy, sx)
            else:
                print("Stop")
                break
    elif d == "S":
        if m == "L":
            sx += 1
            if sx < W + 1 and s[sy][sx] == ".":
                d = "E"
                print(sy, sx)
            else:
                print("Stop")
                break
        elif m =="R":
            sx -= 1
            if sx >= 0  and s[sy][sx] == ".":
                d = "W"
                print(sy, sx)
            else:
                print("Stop")
                break
    elif d == "E":
        if m == "L":
            sy -= 1
            if sy >= 0 and s[sy][sx] == ".":
                d = "N"
                print(sy, sx)
            else:
                print("No")
        elif m =="R":
            sy += 1
            if sy < H + 1 and s[sy][sx] == ".":
                d = "S"
                print(sy, sx)
            else:
                print("Stop")
                break