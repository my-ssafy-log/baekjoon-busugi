###### 입력
import sys
sys.stdin = open('topological_sort/1766/sample_input.txt')
###### 입력 끝

import sys
from collections import defaultdict
from heapq import heappush, heappop

def readline():
    return sys.stdin.readline().rstrip()

N, M = map(int, readline().split())

graph = defaultdict(list)
indegrees = [0] * (N+1)

for _ in range(M):
    p, c = map(int, readline().split())
    graph[p].append(c)
    indegrees[c] += 1

hq = []
for v in range(1, N+1):
    if indegrees[v] == 0:
        heappush(hq, v)

res = []
while hq:
    cur = heappop(hq)
    res.append(cur)
    for nbr in graph[cur]:
        indegrees[nbr] -= 1
        if indegrees[nbr] == 0:
            heappush(hq, nbr)
print(*res)
