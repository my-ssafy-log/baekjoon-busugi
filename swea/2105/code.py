import sys

sys.stdin = open('sample_input.txt', 'r')

#
# N x N에 디저트 카페가 NxN개 모여있다.
# 요소의 숫자는 디저트 카페에서 팔고 있는 디저트 종류를 의미한다.
# 요소 사이에는 대각선으로 이동할 수 있는 길이 있다.
#
# 디저트 카페를 방문하는데 방문하는 규칙은
# 꼭짓점을 제외한 모든 칸에서 대각선으로 이동하며 사각형을 그리며 방문해 원래 위치로 돌아온다.
# 이때 방문한 요소들의 디저트 종류 (숫자가) 같은게 있으면 안된다.
# 가장 많은 카페에 방문한 최대 길이를 구해야한다.
#
# ### 입력
# 태케 50
# N (4 <= N <= 20)
# N x N 2차원 배열 디저트 종류(요소) (1 <= 요소 <= 100)
#
from pprint import pprint

T = int(input())
D = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

for t in range(T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    def is_corner(x, y):
        return (x == 0 and y == 0 or
                x == 0 and y == N-1 or
                x == N-1 and y == 0 or
                x == N-1 and y == N-1)

    def is_out_of_mat(x, y):
        return not (0 <= x < N and 0 <= y < N)

    max_v = 0
    # 시작을 오른쪽 하단으로 이동하는 것을 시작
    for i in range(N-2):
        for j in range(1, N-1):
            X, Y = i, j
            # print('start', X, Y)
            total = 0
            visited = [matrix[X][Y]]

            def dfs(x, y, d, visited, step=1):
                global total
                # print(f'step:({step})', x, y, D[d])
                if i - x == y - j:
                    visited = list(visited)
                    while True:
                        nx = x - 1
                        ny = y + 1
                        if nx == i and ny == j:
                            total = max(total, len(visited))
                            return
                        if matrix[nx][ny] in visited:
                            return
                        visited.append(matrix[nx][ny])
                        x = nx
                        y = ny
                    return

                nx, ny = x + D[d][0], y + D[d][1]
                if not (is_corner(nx, ny) or
                        is_out_of_mat(nx, ny) or
                        matrix[nx][ny] in visited):
                    dfs(nx, ny, d, visited + [matrix[nx][ny]], step+1)

                if d == 2:
                    return

                nx, ny = x + D[d+1][0], y + D[d+1][1]
                if not (is_corner(nx, ny) or
                        is_out_of_mat(nx, ny) or
                        matrix[nx][ny] in visited):
                    dfs(nx, ny, d+1, visited + [matrix[nx][ny]], step+1)

            nx, ny = X + 1, Y + 1
            if matrix[nx][ny] in visited:
                continue
            visited.append(matrix[nx][ny])

            dfs(nx, ny, 0, visited)
            max_v = max(max_v, total)

    print(f"#{t+1}", max_v if max_v else -1)
