import heapq

N = 7
M = 11
edges = [
    (1, 7, 12),
    (1, 4, 28),
    (1, 2, 67),
    (1, 5, 17),
    (2, 4, 24),
    (2, 5, 62),
    (3, 5, 20),
    (3, 6, 37),
    (4, 7, 13),
    (5, 6, 45),
    (5, 7, 73),
]

graph = [[] for _ in range(N+1)]
for a, b, w in edges:
    graph[a].append((b, w))
    graph[b].append((a, w))

start = 1
min_q = [(w, start, nbr) for nbr, w in graph[start]]
heapq.heapify(min_q)

visited = [False] * (N+1)
visited[start] = True

mst = []
while min_q:
    w, start, end = heapq.heappop(min_q)
    if visited[end]: continue
    visited[end] = True
    mst.append((start, end, w))

    for nbr, nbr_w in graph[end]:
        if visited[nbr]: continue
        heapq.heappush(min_q, (nbr_w, end, nbr))

print(mst)
print(sum(x[2] for x in mst))  # 123