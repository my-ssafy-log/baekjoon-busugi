import sys

sys.stdin = open('sample_input.txt', 'r')

#
# N x N (6 <= N <= 20)
# 지형 높이 (1 <= 지형 높이 <= 6)
# 경사로 길이: X (2 <= X <= 4), 높이: 1
# 높이가 있는 구간엔 무조건 경사로 설치
# 경사로는 하나만 설치 가능
# 경사로는 설치 안 할수도 있음
#
#
#
#
# 3 2 2 2 2 2 2 2 3     k = 4

T = int(input())

for t in range(T):
    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for _ in range(2):
        for i, row in enumerate(board):
            flag = 'UP'
            up_cnt = 1
            down_cnt = 0

            for j in range(N - 1):
                if row[j] - row[j+1] == 0:
                    if flag == 'DOWN':
                        down_cnt += 1

                        if down_cnt == X:
                            flag = 'UP'
                            down_cnt = 0
                            up_cnt = 0

                    elif flag == 'UP':
                        up_cnt += 1
                elif row[j] - row[j+1] == 1:
                    if down_cnt == 0:
                        flag = 'DOWN'
                        up_cnt = 0
                        down_cnt = 1
                    else:
                        break
                elif row[j] - row[j+1] == -1:
                    if up_cnt >= X:
                        flag = 'UP'
                        up_cnt = 1
                        down_cnt = 0
                    else:
                        break
                else:
                    break
                if j == N-2 and down_cnt > 0:
                    break
            else:
                # print("best", i)
                cnt += 1
        # print()
        board = list(zip(*board))
    print(f"#{t+1}", cnt)