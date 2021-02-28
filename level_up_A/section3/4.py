H, W, sy, sx, N = map(int,input().split())
d = "N"
s = [list(input()) for _ in range(H)]

for i in range(N):
    l = input().split()
    m = l[0]
    num = int(l[1])
    if d == "N":
        for j in range(num):
            if m == "L":
                sx = sx - num
                if sx >= 0 and s[sy][sx] == ".":
                    d = "W"
                    print(sy, sx)
                    break
                else:
                    sx = 0
                    print(sy, sx)
                    print("Stop")
                    break
            elif m =="R":
                sx = sx + num
                if sx < W + 1  and s[sy][sx] == ".":
                    d = "E"
                    print(sy, sx)
                else:
                    sx = W
                    print(sy, sx)
                    print("Stop")
                    break
        else:
            continue
        break
    elif d == "W":
        for j in range(num):
            if m == "L":
                sy = sy + num
                if sy < H + 1 and s[sy][sx] == ".":
                    d = "S"
                    print(sy, sx)
                    break
                else:
                    sy = H
                    print(sy, sx)
                    print("Stop")
                    break
            elif m =="R":
                sy = sy - num
                if sy >= 0  and s[sy][sx] == ".":
                    d = "N"
                    print(sy, sx)
                else:
                    sy = 0
                    print(sy, sx)
                    print("Stop")
                    break
        else:
            continue
        break
    elif d == "S":
        for j in range(num):
            if m == "L":
                sx = sx + num
                if sx < W + 1 and s[sy][sx] == ".":
                    d = "E"
                    print(sy, sx)
                    break
                else:
                    sx = W
                    print(sy, sx)
                    print("Stop")
                    break
            elif m =="R":
                sx = sx - num
                if sx >= 0  and s[sy][sx] == ".":
                    d = "W"
                    print(sy, sx)
                else:
                    sx = 0
                    print(sy, sx)
                    print("Stop")
                    break
        else:
            continue
        break
    elif d == "E":
        for j in range(num):
            if m == "L":
                sy = sy - num
                if sy >= 0 and s[sy][sx] == ".":
                    d = "N"
                    print(sy, sx)
                    break
                else:
                    sy = 0
                    print(sy, sx)
                    print("Stop")
            elif m =="R":
                sy = sy + num
                if sy < H + 1 and s[sy][sx] == ".":
                    d = "S"
                    print(sy, sx)
                else:
                    sy = H
                    print(sy, sx)
                    print("Stop")
                    break
        else:
            continue
        break