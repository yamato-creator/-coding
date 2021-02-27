H, W, sy, sx, d, m = input().split()
H = int(H)
W = int(W)
sy = int(sy)
sx = int(sx)

s = [list(input()) for _ in range(H)]
if d == "N":
    if m == "L":
        sx -= 1
        if sy > 0 and s[sy][sx] == ".":
            print("Yes")
        else:
            print("No")
    elif m =="R":
        sx += 1
        if sy < W + 1  and s[sy][sx] == ".":
            print("Yes")
        else:
            print("No")
if d == "W":
    if m == "L":
        sy += 1
        if sy < H + 1 and s[sy][sx] == ".":
            print("Yes")
        else:
            print("No")
    elif m =="R":
        sy -= 1
        if sy < 0  and s[sy][sx] == ".":
            print("Yes")
        else:
            print("No")
if d == "S":
    if m == "L":
        sx += 1
        if sy < W + 1 and s[sy][sx] == ".":
            print("Yes")
        else:
            print("No")
    elif m =="R":
        sx -= 1
        if sy > 0  and s[sy][sx] == ".":
            print("Yes")
        else:
            print("No")
if d == "E":
    if m == "L":
        sy += 1
        if sy < H + 1 and s[sy][sx] == ".":
            print("Yes")
        else:
            print("No")
    elif m =="R":
        sy -= 1
        if sy > 0 and s[sy][sx] == ".":
            print("Yes")
        else:
            print("No")