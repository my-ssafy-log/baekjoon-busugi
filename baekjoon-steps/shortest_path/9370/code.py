import sys
import heapq

INF = float('inf')

def readline():
    return sys.stdin.readline().rstrip()

T = int(readline())

for tc in range(T):
    n, m, t = map(int, readline().split())
    s, g, h = map(int, readline().split())

    graph = {i: {} for i in range(1, n+1)}
    goals = []
    
    for _ in range(m):
        a, b, d = map(int, readline().split())
        graph[a][b] = graph[b][a] = d

    for _ in range(t):
        goals.append(int(readline()))

    def dijkstra(start):
        d = [INF] * (n+1)
        d[start] = 0
        prev = [[] for _ in range(n+1)]
        queue = [(0, start)]
        while queue:
            dist, cur = heapq.heappop(queue)
            if dist > d[cur]:
                continue
            for nbr in graph[cur]:
                nbr_d = graph[cur][nbr]
                next_d = dist + nbr_d
                
                if next_d < d[nbr]:
                    d[nbr] = next_d
                    prev[nbr] = [cur]
                    heapq.heappush(queue, (next_d, nbr))
                elif next_d == d[nbr]:
                    prev[nbr].append(cur)
        return d, prev
    d, prev = dijkstra(s)

    possibles = []
    # goals 에서부터 역추적하며 g - h 를 지났는지 확인
    for goal in goals:
        queue = [goal]
        
        while queue:
            cur = queue.pop()

            for nbr in prev[cur]:
                if (nbr, cur) == (g, h) or (nbr, cur) == (h, g):
                    possibles.append(goal)
                    queue = []  # while 문 벗어나기 위함
                    break
                queue.append(nbr)
    
    # print(d)
    # print(prev)
    print(*sorted(possibles))
