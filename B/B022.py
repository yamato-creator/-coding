M, N, K = map(int, input().split())

s = [input() for _ in range(K)]

power = {str(x): 0 for x in range(1, M + 1)}
power['voter'] = K

for i in s:
    for key, value in power.items():
        if value > 0:
            power[key] = power[key] - 1
            power[i] = power[i] + 1

del power['voter']

max_value = max(power.values())
result =  [key for key in power if power[key] == max_value]

for result in result:
    print(result)
