import sys
from collections import deque

def readline():
    return sys.stdin.readline().rstrip()

V = int(readline())

adj = [[] for _ in range(V+1)]
for _ in range(V-1):
    u, v, w = map(int, readline().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

def bfs(start):
    visited = [-1] * (V+1)
    visited[start] = 0
    queue = deque([start])

    max_d = 0
    farthest = 1
    while queue:
        cur = queue.popleft()
        for nbr, nbr_w in adj[cur]:
            if visited[nbr] != -1: continue
            queue.append(nbr)
            visited[nbr] = visited[cur] + nbr_w
            if visited[nbr] > max_d:
                max_d = visited[nbr]
                farthest = nbr
    return farthest, max_d

farthest, _ = bfs(1)
_, diameter = bfs(farthest)

print(diameter)
