from heapq import heappop, heappush

INF = float('inf')

N, K = map(int, input().split())

visited = [INF] * 100001
visited[N] = 0
queue = [(0, N)]

while queue:
    dist, cur = heappop(queue)
    if cur + 1 <= 100000 and visited[cur+1] > dist + 1:
        visited[cur+1] = dist + 1
        heappush(queue, (dist + 1, cur + 1))
    if cur - 1 >= 0 and visited[cur-1] > dist + 1:
        visited[cur-1] = dist + 1
        heappush(queue, (dist + 1, cur - 1))
    if cur * 2 <= 100000 and visited[cur*2] > dist:
        visited[cur*2] = dist
        heappush(queue, (dist, cur * 2))

print(visited[K])
