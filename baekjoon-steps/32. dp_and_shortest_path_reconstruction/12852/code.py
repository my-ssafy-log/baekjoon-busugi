from heapq import heappush, heappop

N = int(input())

d = [float('inf')] * (N+1)
nxt = [None] * (N+1)
d[N] = 0
min_q = [(0, N)]
while min_q:
    dist, cur = heappop(min_q)

    if d[cur] < dist: continue
    if cur <= 1: continue

    if d[cur - 1] > dist + 1:
        d[cur - 1] = dist + 1
        heappush(min_q, (dist + 1, cur - 1))
        nxt[cur - 1] = cur
        
    if cur % 3 == 0 and d[cur // 3] > dist + 1:
        d[cur // 3] = dist + 1
        heappush(min_q, (dist + 1, cur // 3))
        nxt[cur // 3] = cur
        
    if cur % 2 == 0 and d[cur // 2] > dist + 1:
        d[cur // 2] = dist + 1
        heappush(min_q, (dist + 1, cur // 2))
        nxt[cur // 2] = cur

path = [1]
cur = 1
while nxt[cur] != None:
    path.append(nxt[cur])
    cur = nxt[cur]

print(len(path) - 1)
print(*list(reversed(path)))
