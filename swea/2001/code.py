T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            total = 0
            for k in range(i, i + M):
                for l in range(j, j + M):
                    total += board[k][l]
            max_v = max(max_v, total)
    print(f"#{t+1} {max_v}")