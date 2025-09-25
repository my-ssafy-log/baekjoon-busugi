#### 입력
import sys
sys.stdin = open('shortest_path/5719/sample_input2.txt')
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
    reversed_graph = [[] for _ in range(N)]
    dropped = set()

    for _ in range(M):
        U, V, P = map(int, readline().split())
        graph[U].append((V, P))
        reversed_graph[V].append((U, P))
    
    def dijkstra(start):
        d = [INF] * N
        d[start] = 0
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
        return d

    d = dijkstra(S)
    stack = [D]
    while stack:
        cur = stack.pop()
        if cur == S:
            continue
        for prev, prev_d in reversed_graph[cur]:
            if d[prev] + prev_d == d[cur] and (prev, cur) not in dropped:
                dropped.add((prev, cur))
                stack.append(prev)
    
    d = dijkstra(S)
    print(d[D] if d[D] != INF else -1)
