import sys
from heapq import heappop, heappush

def readline():
    return sys.stdin.readline().rstrip()

INF = float('inf')

n = int(readline())
m = int(readline())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    A, B, w = map(int, readline().split())
    adj[A].append((B, w))
S, E = map(int, readline().split())

def dijkstra(start):
    prev = [None] * (n+1)
    d = [INF] * (n+1)
    d[start] = 0
    min_q = [(0, start)]
    while min_q:
        dist, cur = heappop(min_q)
        if d[cur] < dist:
            continue

        for nbr, nbr_w in adj[cur]:
            if d[nbr] > dist + nbr_w:
                prev[nbr] = cur
                d[nbr] = dist + nbr_w
                heappush(min_q, (dist + nbr_w, nbr))
    return d, prev

d, prev = dijkstra(S)
path = [E]
cur = E
while prev[cur] is not None:
    cur = prev[cur]
    path.append(cur)
print(d[E])
print(len(path))
print(*reversed(path))
