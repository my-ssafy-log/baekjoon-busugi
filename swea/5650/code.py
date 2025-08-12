import sys
sys.stdin = open('sample_input2.txt', 'r')

D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
D_IDX_MAP = {
    (-1, 0): 0,
    (1, 0): 1,
    (0, -1): 2,
    (0, 1): 3
}
BLOCK_DIR = ((), (1, 3, 0, 2), (3, 0, 1, 2), (2, 0, 3, 1), (1, 2, 3, 0), (1, 0, 3, 2))

T = int(input())

for t in range(T):
    N = int(input())
    board = []

    wormhole = {}
    get_teleport_pos = {}

    for i in range(N):
        row = list(map(int, input().split()))
        for j, cell in enumerate(row):
            if 6 <= cell <= 10:
                wormhole.setdefault(cell, [])
                wormhole[cell].append((i, j))
        board.append(row)

    for key, value in wormhole.items():
        get_teleport_pos[value[0]] = value[1]
        get_teleport_pos[value[1]] = value[0]


    def is_out_of_board(x, y):
        return not (0 <= x < N and 0 <= y < N)


    def is_block(x, y):
        return 1 <= board[x][y] <= 5


    def is_wormhole(x, y):
        return 6 <= board[x][y] <= 10


    def is_blackhole(x, y):
        return board[x][y] == -1


    def reverse_dir(dx, dy):
        return -dx, -dy


    def block_reflect_dir(dx, dy, block):
        d_idx = D_IDX_MAP[(dx, dy)]
        rd_idx = BLOCK_DIR[block][d_idx]
        return D[rd_idx]


    point_memo = {}

    max_point = -float('inf')
    # 시작 위치 찾기
    for start_x in range(N):
        for start_y in range(N):
            if board[start_x][start_y] != 0:
                continue

            for start_dx, start_dy in D:
                dx, dy = start_dx, start_dy
                x, y = start_x, start_y

                point = 0

                prev_memo = ((start_x - abs(start_dx), start_y - abs(start_dy)), (start_dx, start_dy))
                if prev_memo in point_memo:
                    continue

                while True:
                    x += dx
                    y += dy

                    if (x, y) == (start_x, start_y):
                        break
                    if is_out_of_board(x, y):
                        dx, dy = reverse_dir(dx, dy)
                        point += 1
                    elif is_block(x, y):
                        dx, dy = block_reflect_dir(dx, dy, board[x][y])
                        point += 1
                    elif is_wormhole(x, y):
                        x, y = get_teleport_pos[(x, y)]
                    elif is_blackhole(x, y):
                        break

                point_memo[((start_x, start_y), (start_dx, start_dy))] = point
                max_point = max(max_point, point)
    print(f"#{t + 1} {max_point}")