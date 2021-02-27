H, W, sy, sx, m = input().split()
H = int(H)
W = int(W)
sy = int(sy)
sx = int(sx)

s = [list(input()) for _ in range(H)]
if m == "N":
    sy -= 1
    if sy != -1:
        if s[sy][sx] == ".":
            print("Yes")
        else:
            print("No")
    else:
        print("No")
if m == "W":
    sx -= 1
    if sx != -1:
        if s[sy][sx] == ".":
            print("Yes")
        else:
            print("No")
    else:
        print("No")
if m == "S":
    sy += 1
    if sy != H + 1:
        if s[sy][sx] == ".":
            print("Yes")
        else:
            print("No")
    else:
        print("No")
if m == "E":
    sx += 1
    if sx != W + 1:
        if s[sy][sx] == ".":
            print("Yes")
        else:
            print("No")
    else:
        print("No")