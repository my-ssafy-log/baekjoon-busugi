from collections import defaultdict
from heapq import heappush, heappop

INF = float('inf')

N, E = map(int, input().split())
graph = {i: defaultdict(lambda: INF) for i in range(N+1)}

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = graph[b][a] = c

v1, v2 = map(int, input().split())

def dijk(start):
    d = [INF] * (N+1)
    d[start] = 0
    prev = [None] * (N+1)
    queue = [(0, start)]
    while queue:
        dist, cur = heappop(queue)
        if dist > d[cur]:
            continue
        for nbr in graph[cur]:
            nbr_w = graph[cur][nbr]
            nbr_dist = dist + nbr_w
            if nbr_dist < d[nbr]:
                d[nbr] = nbr_dist
                heappush(queue, (nbr_dist, nbr))
                prev[nbr] = cur
    return d

d_v1 = dijk(v1)
d_v2 = dijk(v2)

min_d1 = d_v1[1] + d_v1[v2] + d_v2[N]
min_d2 = d_v2[1] + d_v2[v1] + d_v1[N]
min_d = min(min_d1, min_d2)
print(min_d if min_d != INF else -1)
