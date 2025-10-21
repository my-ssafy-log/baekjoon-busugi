from collections import deque

N, K = map(int, input().split())

INF = float('inf')

prev = [None] * 200001
d = [INF] * 200001
d[N] = 0
queue = deque([N])

while queue:
    cur = queue.popleft()
    dist = d[cur]
    if cur-1 >= 0 and d[cur-1] > dist + 1:
        d[cur-1] = dist + 1
        prev[cur-1] = cur
        queue.append(cur-1)
    if cur+1 <= 200000 and d[cur+1] > dist + 1:
        d[cur+1] = dist + 1
        prev[cur+1] = cur
        queue.append(cur+1)
    if cur*2 <= 200000 and d[cur*2] > dist + 1:
        d[cur*2] = dist + 1
        prev[cur*2] = cur
        queue.append(cur*2)

cur = K
path = [cur]

while prev[cur] is not None:
    cur = prev[cur]
    path.append(cur)

print(len(path) - 1)
print(*reversed(path))
