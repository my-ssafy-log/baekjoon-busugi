import sys
sys.stdin = open('graphs_and_tours/7562/sample_input.txt')

import sys
from collections import deque

def readline():
    return sys.stdin.readline().rstrip()

T = int(readline())

for t in range(T):
    N = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    
    visited = [[-1] * N for _ in range(N)]
    visited[start[0]][start[1]] = 0
    queue = deque([start])

    def out_of_range(x, y):
        return not (0 <= x < N and 0 <= y < N)

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]:
            nx, ny = x + dx, y + dy
            if out_of_range(nx, ny):
                continue
            if visited[nx][ny] != -1:
                continue
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))
            if (nx, ny) == end:
                break

    print(visited[end[0]][end[1]])
