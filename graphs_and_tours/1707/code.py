import sys
sys.stdin = open('graphs_and_tours/1707/sample_input.txt')

import sys

def readline():
    return sys.stdin.readline().rstrip()

K = int(readline())

for k in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    is_bipartite = True  # 이분 그래프인가? 변수

    # color는 1과 2를 반복하며 visited에 색상을 삽입함
    def dfs(cur, color):
        stack = [(cur, color)]
        global is_bipartite

        visited[cur] = color

        while stack:
            cur, color = stack.pop()
            for nbr in graph[cur]:
                if visited[nbr]:  # 만약 이미 색상이 삽입된 상태인데
                    if visited[nbr] == color:  # cur과 인접한 nbr가 cur의 color와 같다면
                        is_bipartite = False
                        return
                    continue

                stack.append((nbr, 3 - color))
                visited[nbr] = 3 - color

    for v in range(1, V+1):
        if visited[v]: continue
        dfs(v, 1)
    print('YES' if is_bipartite else 'NO')
