N = int(input())

x, y = map(int, input().split())
x, y = x - 1, y - 1

board = [[0] * (2 ** N) for _ in range(2 ** N)]
board[x][y] = -1
N = 2 ** (N-1)

ignore = [None, (1, 1), (0, 1), (0, 0), (1, 0)]

tile = 1
def dfs(ty, pos, size, rec):
    global tile
    if size == 1:
        ign_pos = (pos[0] + ignore[ty][0], pos[1] + ignore[ty][1])
        for i in range(pos[0], pos[0] + 2):
            for j in range(pos[1], pos[1] + 2):
                if (i, j) == ign_pos:
                    continue
                board[i][j] = tile
        tile += 1
        return

    part_size = size // 2
    part_ty_pos = ((x % size) // part_size, (y % size) // part_size)
    part_ty = ty_dict[part_ty_pos]

    if ty == 1:
        dfs(1, pos, part_size, False)
        dfs(1, (pos[0] + part_size, pos[1] + part_size), part_size, False)
        dfs(4, (pos[0], pos[1] + size), part_size, False)
        dfs(2, (pos[0] + size, pos[1]), part_size, False)

        if rec:
            dfs(part_ty,
                (pos[0] + size, pos[1] + size),
                part_size,
                True)
    if ty == 2:
        dfs(2, (pos[0] + part_size, pos[1] + part_size), part_size, False)
        dfs(2, (pos[0] + size, pos[1]), part_size, False)
        dfs(1, pos, part_size, False)
        dfs(3, (pos[0] + size, pos[1] + size), part_size, False)

        if rec:
            dfs(part_ty,
               (pos[0], pos[1] + size),
               part_size,
               True)

    if ty == 3:
        dfs(3, (pos[0] + part_size, pos[1] + part_size), part_size, False)
        dfs(3, (pos[0] + size, pos[1] + size), part_size, False)
        dfs(4, (pos[0], pos[1] + size), part_size, False)
        dfs(2, (pos[0] + size, pos[1]), part_size, False)

        if rec:
            dfs(part_ty,
               (pos[0], pos[1]),
               part_size,
               True)

    if ty == 4:
        dfs(4, (pos[0] + part_size, pos[1] + part_size), part_size, False)
        dfs(4, (pos[0], pos[1] + size), part_size, False)
        dfs(1, pos, part_size, False)
        dfs(3, (pos[0] + size, pos[1] + size), part_size, False)

        if rec:
            dfs(part_ty,
               (pos[0] + size, pos[1]),
               part_size,
               True)

ty_dict = {
    (1, 1): 1,
    (0, 1): 2,
    (0, 0): 3,
    (1, 0): 4
}
# print(N)
dfs(ty_dict[(x // N, y // N)], (0, 0), N, True)

for row in list(zip(*board))[::-1]:
    print(*row)
