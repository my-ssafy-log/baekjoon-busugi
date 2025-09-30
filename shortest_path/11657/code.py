N, M = map(int, input().split())

graph = {i: {} for i in range(1, N+1)}
for _ in range(M):
    A, B, C = map(int, input().split())
    if B in graph[A]:
        C = min(graph[A][B], C)
    graph[A][B] = C

INF = float('inf')

def bellman_ford(start):
    dist = [INF] * (N+1)
    dist[start] = 0
    for _ in range(N-1):
        updated = False
        for u in graph:
            for v in graph[u]:
                if dist[u] != INF and dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
                    updated = True
        if not updated:
            break
    
    # 음의 사이클 있는지 확인
    for u in graph:
        for v in graph[u]:
            if dist[u] != INF and dist[u] + graph[u][v] < dist[v]:
                return None
    return dist

dist = bellman_ford(1)

if dist is None:
    print(-1)
else:
    for v in dist[2:]:
        print(v if v != INF else -1)
