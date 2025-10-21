S1 = input()
S2 = input()
N = len(S1)
M = len(S2)

board = [
    [0] * (N + 1) for _ in range(M+1)
]

for i in range(1, M+1):
    for j in range(1, N+1):
        board[i][j] = max(board[i-1][j], board[i][j-1], board[i-1][j-1] + int(S1[j-1] == S2[i-1]))

cur = board[M][N]
i, j = M, N

res = []
while cur != 0:
    if board[i-1][j] == cur:
        i -= 1
    elif board[i][j-1] == cur:
        j -= 1
    else:
        res.append(S1[j-1])
        i -= 1
        j -= 1
        cur = board[i][j]

# print(*board, sep='\n')

print(len(res))
print(*reversed(res), sep='')
