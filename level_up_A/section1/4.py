h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for y in range(h):
    for x in range(w):
        if y == 0:
            #  上端の場合
            if s[y + 1][x] == "#":
                print(y, x)
        elif y == h - 1:
            #  下端の場合
            if s[y - 1][x] == "#":
                print(y, x)
        elif s[y-1][x] == "#" and s[y + 1][x] == "#":
            print(y,x)