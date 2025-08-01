import sys
from collections import deque

def readline():
    return sys.stdin.readline().rstrip()

N, K = map(int, readline().split())

if N >= K:
    print(N - K)
else:
    visited = [False] * 200_001
    queue = deque()
    queue.append(N)
    is_complete = False
    step = 0
    
    while not is_complete:
        size = len(queue)
        # print(queue)

        for _ in range(size):
            n = queue.popleft()
            visited[n] = True

            if n * 2 <= 200000 and not visited[n*2]:
                queue.append(n*2)
            if n+1 <= K and not visited[n+1]:
                queue.append(n+1)
            if n-1 >= 0 and not visited[n-1]:
                queue.append(n-1)

            if n*2 == K or n+1 == K or n-1 == K:
                is_complete = True
                break
        step += 1
    print(step)