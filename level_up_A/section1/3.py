h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for y in range(h):
    for x in range(w):
        if x == 0:
            #  左端の場合
            if s[y][x+1] == "#":
                print(y, x)
        elif x == w - 1:
            #  右端の場合
            if s[y][x-1] == "#":
                print(y, x)
        elif s[y][x - 1] == "#" and s[y][x + 1] == "#":
            print(y,x)