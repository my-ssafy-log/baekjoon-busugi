INF = float('inf')

N = int(input())
M = int(input())

graph = [[INF] * (N+1) for i in range(0, N+1)]
for i in range(N+1): graph[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, N+1):
    print(*[v if v != INF else 0 for v in graph[i][1:]])
