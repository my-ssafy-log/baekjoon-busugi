#### 입력
import sys
sys.stdin = open('shortest_path/5719/sample_input.txt')
####

import sys
import heapq

INF = float('inf')

def readline():
    return sys.stdin.readline().rstrip()


while True:
    N, M = map(int, readline().split())
    if N == M == 0:
        break
    S, D = map(int, readline().split())

    graph = [[] for _ in range(N)]
    dropped = set()

    for _ in range(M):
        U, V, P = map(int, readline().split())
        graph[U].append((V, P))
    
    def dijkstra(start):
        d = [INF] * N
        d[start] = 0
        prev = [[] for _ in range(N)]
        mq = [(0, start)]
        while mq:
            dist, cur = heapq.heappop(mq)

            if dist > d[cur]:
                continue

            for nbr, nbr_d in graph[cur]:
                if (cur, nbr) in dropped:
                    continue
                next_d = dist + nbr_d
                if next_d < d[nbr]:
                    d[nbr] = next_d
                    heapq.heappush(mq, (next_d, nbr))
                    prev[nbr] = [cur]
                elif next_d == d[nbr]:
                    prev[nbr].append(cur)
        return d, prev

    _, prev = dijkstra(S)
    stack = [D]
    while stack:
        cur = stack.pop()
        for nbr in prev[cur]:
            if (nbr, cur) in dropped:
                continue
            dropped.add((nbr, cur))
            stack.append(nbr)
    d, _ = dijkstra(S)
    print(d[D] if d[D] != INF else -1)
