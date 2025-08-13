import sys

sys.stdin = open('sample_input.txt', 'r')

#
# 출력: 탈주범이 있을 수 있는 위치의 '개수'
# 지하 터널 종류 총 7가지
#
# 1: 상하좌우
# 2: 상하
# 3: 좌우
# 4: 상우
# 5: 하우
# 6: 하좌
# 7: 상좌
#
# ### 입력
# 태케 50
# 세로 N x 가로 M (5 <= N, M <= 50)
# 멘홀 뚜껑 위치 R, C (0 <= R <= N-1, 0 <= C <= M-1)
# 맨홀 뚜겅은 항상 터널 위에 있음
# 탈출 소요 시간 L (1 <= L <= 20)
#
#
#
#

dx_dict = {
    1: [(-1, 0), (1, 0), (0, -1), (0, 1)],  # 상하좌우
    2: [(-1, 0), (1, 0)],  # 상하
    3: [(0, -1), (0, 1)],  # 좌우
    4: [(-1, 0), (0, 1)],  # 상우
    5: [(1, 0), (0, 1)],  # 하우
    6: [(1, 0), (0, -1)],  # 하좌
    7: [(-1, 0), (0, -1)],  # 상좌
}

from collections import deque

T = int(input())

for t in range(T):
    N, M, R, C, L = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    cnt = 1
    queue = deque()
    queue.append((R, C))
    visited = set()
    visited.add((R, C))

    def can_go(pos, entry_dir):
        x, y = pos
        if not (0 <= x < N and 0 <= y < M):
            return False
        ttype = matrix[x][y]
        entry_type_dict = {
            (-1, 0): [1, 2, 5, 6],
            (1, 0): [1, 2, 4, 7],
            (0, -1): [1, 3, 4, 5],
            (0, 1): [1, 3, 6, 7]
        }
        return ttype in entry_type_dict[entry_dir]

    for l in range(1, L):
        new_queue = deque()

        while queue:
            r, c = queue.popleft()
            ttype = matrix[r][c]
            # 상하좌우 방문하지 않은 이동할 수 있는 곳 찾고 추가하기
            for dx, dy in dx_dict[ttype]:
                nx = r + dx
                ny = c + dy
                if (nx, ny) not in visited and can_go((nx, ny), (dx, dy)):
                    new_queue.append((nx, ny))
                    visited.add((nx, ny))
        queue = new_queue
        # print(queue)
    # print(visited)
    print(f"#{t+1} {len(visited)}")
    # print('-' * 100)
