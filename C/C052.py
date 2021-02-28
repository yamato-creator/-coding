H, W = map(int, input().split())
dx, dy = map(int, input().split())

print(abs(H * dy) + abs(W * dx) - abs(dx * dy))