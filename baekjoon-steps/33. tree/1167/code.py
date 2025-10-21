import sys
from collections import deque

def readline():
    return sys.stdin.readline().rstrip()

V = int(readline())

adj = [[] for _ in range(V+1)]
for _ in range(V):
    u, *args, eol = map(int, readline().split())
    for i in range(0, len(args), 2):
        v, w = args[i], args[i+1]
        adj[u].append((v, w))

# print(*adj, sep='\n')

def bfs(start):
    visited = [-1] * (V+1)
    visited[start] = 0
    queue = deque([start])

    max_d = -1
    farthest = None
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
# print(farthest)
_, diameter = bfs(farthest)

print(diameter)
