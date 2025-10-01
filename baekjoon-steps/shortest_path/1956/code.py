import sys
from heapq import heappush, heappop

def readline():
    return sys.stdin.readline().rstrip()

V, E = map(int, readline().split())

INF = float('inf')
graph = [[INF] * (V+1) for _ in range(V+1)]

for i in range(V+1):
    graph[i][i] = 0

for _ in range(E):
    a, b, c = map(int, readline().split())
    graph[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

min_cycle = INF
for i in range(1, V):
    for j in range(i+1, V+1):
        if i == j: continue
        cycle = graph[i][j] + graph[j][i]
        min_cycle = min(min_cycle, cycle)

print(min_cycle if min_cycle != INF else -1)
