x, y, n = map(int, input().split())

loop_cnt = 0  # 方位が2回カウントされるかチェックする変数
d_cnt = 0  # 方位リストをカウントする
cnt = 0 #進む距離をカウント
d_count = 1 #同じ方向に何マス進むか
d_list = ["E", "S", "W", "N"]
compass = d_list[0]
while True:
    for j in range(d_count):
        if compass == "N":
            y -= 1
        elif compass == "W":
            x -= 1
        elif compass == "E":
            x += 1
        elif compass == "S":
            y += 1
        cnt += 1
        if cnt == n:
            break
    else:
        d_cnt += 1
        compass = d_list[d_cnt % 4]
        loop_cnt += 1
        # 方位が2回変わったなら同じ方角で進む距離を延ばす
        if loop_cnt % 2 == 0:
            d_count += 1
        continue
    break

print(x, y)