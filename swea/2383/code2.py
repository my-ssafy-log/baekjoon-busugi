import sys

sys.stdin = open('sample_input.txt', 'r')

# 테케 50개
# N x N (4 <= N <= 10)
# 사람 수 1명 ~ 10명
# 계단 입구 반드시 2개
# 계단 길이 2 ~ 10
# 사람 위치, 계단 입구 위치 겹치지 X
#
# ### 입력
# N
# N x N 2차원 배열
#
#

T = int(input())

for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    pos_list = []
    stairs_list = []
    stairs_time_list = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                pos_list.append((i, j))
            elif board[i][j] > 1:
                stairs_list.append((i, j))
                stairs_time_list.append(board[i][j])

    stair1_targets = []
    stair2_targets = []

    def get_spend_time(stair_pos, targets, stair_time):
        if not targets:
            return 0
        dist_list = sorted(
            map(
                lambda pos:
                abs(stair_pos[0] - pos[0]) +
                abs(stair_pos[1] - pos[1]),
                targets
            )
        )
        spend_time = max(dist_list[:3]) + stair_time
        for i in range(3, len(dist_list)):
            spend_time = max(dist_list[i - 3] + stair_time, dist_list[i]) + stair_time
        return spend_time

    min_spend_time = float('inf')

    def dfs(step):
        global min_spend_time
        if step == len(pos_list):
            stair1_pos, stair2_pos = stairs_list
            stair1_time, stair2_time = stairs_time_list

            spend_time1 = get_spend_time(stair1_pos, stair1_targets, stair1_time)
            spend_time2 = get_spend_time(stair2_pos, stair2_targets, stair2_time)
            min_spend_time = min(min_spend_time, max(spend_time1, spend_time2))
            return

        stair1_targets.append(pos_list[step])
        dfs(step+1)
        stair1_targets.pop()
        stair2_targets.append(pos_list[step])
        dfs(step+1)
        stair2_targets.pop()

    dfs(0)
    print(f"#{t+1}", min_spend_time+1)
