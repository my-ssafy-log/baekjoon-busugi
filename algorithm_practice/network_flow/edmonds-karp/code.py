import sys
from collections import deque
sys.stdin = open('sample_input.txt', 'r')

N = int(input())  # 노드의 개수
M = int(input())  # 간선의 개수

capacity = [[0] * (N+1) for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

def connect(a, b, c):
    graph[a].append(b)
    graph[b].append(a)
    capacity[a][b] = c

# a노드에서 b노드로 가는 네트워크 용량 정보
for i in range(M):
    a, b, c = map(int, input().split())
    connect(a, b, c)

def max_flow(start, end):
    route = [-1] * (N+1)  # bfs를 수행할 때 방문기록과 함께 i번 노드의 부모를 저장하기 위한 배열
    flow = [[0] * (N+1) for _ in range(N+1)]  # 네트워크 용량에 흐르는 유량을 담는 배열. bfs를 수행하며 매번 갱신됨

    result = 0
    while True:
        route = [-1] * (N+1)
        queue = deque()
        queue.append(start)

        # start에서 end로 가는 경로를 route에 표시
        # start에서 end로 갈 때 보낼 수 있는 네트워크 유량이 남아있는 경우에만 route에 표시
        while queue:
            a = queue.popleft()
            for b in graph[a]:
                if capacity[a][b] - flow[a][b] > 0 and route[b] == -1:
                    route[b] = a
                    queue.append(b)
                    if b == end:
                        break

        if route[end] == -1:  # 더 이상 보낼 수 있는 네트워크 유량이 없어 end에 방문을 못했다면?
            break
        
        # 표시된 route에서 end부터 start까지 올라가며 최소로 보낼 수 있는 네트워크 유량 찾기
        min_flow = float('inf')
        cur_node = end
        while cur_node != start:
            min_flow = min(min_flow, capacity[route[cur_node]][cur_node] - flow[route[cur_node]][cur_node])
            cur_node = route[cur_node]
        
        # end부터 start까지 올라가며 구한 보낼 수 있는 네트워크 유량을 기존 네트워크 유량에 더해줌
        cur_node = end
        while cur_node != start:
            flow[route[cur_node]][cur_node] += min_flow
            flow[cur_node][route[cur_node]] -= min_flow  # 음의 유량도 구하기 위해 반대 방향에는 음의 유량만큼 빼줌
            cur_node = route[cur_node]

        result += min_flow

    return result

print(max_flow(1, 6))
