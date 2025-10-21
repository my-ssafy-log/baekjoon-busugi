N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()
s = 0
e = len(liquids) - 1

min_mixed = float('inf')
min_mixed_liquids = (0, 0)

while s < e:
    mixed = liquids[s] + liquids[e]
    if min_mixed > abs(mixed):
        min_mixed = abs(mixed)
        min_mixed_liquids = (liquids[s], liquids[e])

    if mixed == 0:
        break
    if mixed < 0:
        s += 1
    elif mixed > 0:
        e -= 1

print(min_mixed_liquids[0], min_mixed_liquids[1])
