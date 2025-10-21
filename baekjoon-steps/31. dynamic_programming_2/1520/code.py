import sys; sys.stdin = open('baekjoon-steps/dynamic_programming_2/1520/input.txt')

import sys
sys.setrecursionlimit(10000)

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

cases = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]
impossible = [[False] * N for _ in range(M)]

cnt = 0
def dfs(pos):
    global cnt
    cnt += 1
    if pos == (M-1, N-1):
        return 1
    x, y = pos
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = pos[0] + dx, pos[1] + dy
        if not (0 <= nx < M and 0 <= ny < N): continue
        if board[nx][ny] >= board[x][y]: continue
        if visited[nx][ny]: continue
        if impossible[nx][ny]: continue
        if cases[nx][ny] != 0:
            cases[x][y] += cases[nx][ny]
            continue
        visited[nx][ny] = True
        cases[x][y] += dfs((nx, ny))
        visited[nx][ny] = False
    if cases[x][y] == 0:
        impossible[x][y] = True
    return cases[x][y]

visited[0][0] = True
print(dfs((0, 0)))
