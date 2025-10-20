import sys; sys.stdin = open('input.txt')

import sys

def readline():
    return sys.stdin.readline().rstrip()

N = int(input())

adj = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (N+1)
visited[1] = True
p = [None] * (N+1)
queue = [1]
while queue:
    cur = queue.pop()
    for nbr in adj[cur]:
        if visited[nbr]: continue
        queue.append(nbr)
        visited[nbr] = True
        p[nbr] = cur
print(*p[2:], sep='\n')
