n, m = map(int, input().split())
a, b = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]
from_v, to_v, satisfaction = zip(*edges)

# Please write your code here.
import heapq

adj = [[] for _ in range(n+1)]
for i in range(m):
    u, v, w = from_v[i], to_v[i], satisfaction[i]
    adj[u].append((v, w))
    adj[v].append((u, w))

INF = float('inf')
min_w = [0] * (n+1)
min_w[a] = INF
min_queue = [(-INF, a)]

while min_queue:
    cur_min_w, cur = heapq.heappop(min_queue)
    cur_min_w = -cur_min_w

    if cur == b:
        break

    if min_w[cur] > cur_min_w:
        continue

    for nbr, nbr_w in adj[cur]:
        nxt_min_w = min(nbr_w, cur_min_w)
        if min_w[nbr] < nxt_min_w:
            min_w[nbr] = nxt_min_w
            heapq.heappush(min_queue, (-nxt_min_w, nbr))

print(min_w[b])
