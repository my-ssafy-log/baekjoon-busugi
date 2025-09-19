import sys
from collections import defaultdict
from heapq import heappush, heappop


def readline():
    return sys.stdin.readline().rstrip()


N, M, X = map(int, readline().split())
graph = defaultdict(list)
reversed_graph = defaultdict(list)
for _ in range(M):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))
    reversed_graph[v].append((u, t))

# pprint(graph)
# pprint(reversed_graph)


# 0: X에서 각각의 집으로 돌아가는데 걸리는 시간과
# 1: 각각의 집에서 X로 오는데 걸리는 시간
visited = [[-1, -1] for _ in range(N+1)]
visited[X] = [0, 0]
visited_cnt = 1
# 0번은 X에서 각각의 집으로 돌아가는 방향
# 1번은 집에서 X로 오는 방향
queue = [(0, X, 0), (0, X, 1)]

while queue:
    if visited_cnt == N:
        break
    time, node, direct = heappop(queue)

    if visited[node][direct] == -1:
        continue

    cur_graph = [graph, reversed_graph][direct]

    for nbr, nbr_time in cur_graph[node]:
        next_time = time + nbr_time
        if visited[nbr][direct] == -1 or visited[nbr][direct] > next_time:
            visited[nbr][direct] = next_time
            heappush(queue, (next_time, nbr, direct))

print(sum(max(visited[1:], key=lambda x: x[0] + x[1])))
