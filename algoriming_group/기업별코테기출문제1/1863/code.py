n = int(input())
poss = [tuple(map(int, input().split())) for _ in range(n)]
poss.sort(key=lambda pos: pos[0])

showed = [0]
cnt = 0
for x, height in poss:
    cur = showed[-1]
    if height > cur:
        showed.append(height)
        cnt += 1
    elif height < cur:
        while showed[-1] > height:
            showed.pop()
        if showed[-1] != height:
            showed.append(height)
            cnt += 1
print(cnt)
