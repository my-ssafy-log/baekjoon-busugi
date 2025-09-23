###### 입력
import sys
sys.stdin = open('topological_sort/3665/sample_input.txt')
###### 입력 끝

import sys
from collections import defaultdict, deque

def readline():
    return sys.stdin.readline().rstrip()

T = int(readline())

for _ in range(T):
    N = int(readline())
    arr = list(map(int, input().split()))
    indegrees = [0] * (N+1)

    rank = [0] * (N+1)
    # 랭크 생성 및 위상 정렬을 위한 간선 설치
    graph = defaultdict(set)
    for i, parent in enumerate(arr):
        rank[parent] = i
        for child in arr[i+1:]:
            indegrees[child] += 1
            graph[parent].add(child)

    # 스왑하는 연산
    M = int(readline())
    for _ in range(M):
        u, v = map(int, readline().split())
        if rank[u] > rank[v]:
            indegrees[u] -= 1
            indegrees[v] += 1
            graph[v].discard(u)
            graph[u].add(v)
        else:
            indegrees[v] -= 1
            indegrees[u] += 1
            graph[u].discard(v)
            graph[v].add(u)

    
    queue = deque([])
    for v, indegree in enumerate(indegrees[1:], 1):
        if indegree == 0:
            queue.append(v)
            break

    res = []
    while queue:
        cur = queue.popleft()
        res.append(cur)
        for nbr in graph[cur]:
            indegrees[nbr] -= 1
            if indegrees[nbr] == 0:
                queue.append(nbr)
    if len(res) < N:
        print("IMPOSSIBLE")
    else:
        print(*res)
