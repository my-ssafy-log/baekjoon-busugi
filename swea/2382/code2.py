import sys

sys.stdin = open('sample_input.txt', 'r')

# 테케 50개
# - 미생물 군집의 개수 K (5 <= K <= 1,000)
# - N x N (5 <= N <= 100)
# - 미생물 군집엔 미생물 수 (1 <= 군집 내 미생물수 <= 10,000), 이동방향(상하좌우:1234)이 있다.
#
# N x N 매트 가장자리는 약품처리 돼있는데,
# 미생물이 이동하다 약품에 걸리면 절반 죽음 (소수점 이하 버림)
# 그러다 미생물 수 0 되면 사라짐
# 처음 상태에서 미생물은 약품이 있는 가장자리엔 있지 않음
#
# 미생물 군집들이 이동하다 위치가 겹치면 군집 내 미생물 수 합쳐져 하나의 군집이 됨
# 2개 이상의 군집이 합쳐지면 그만큼 미생물이 더해짐,
# 합쳐질 때 가장 미생물 수가 많은 미생물 군집의 방향이 합쳐진 군집의 방향이 됨
#
# - M시간 (1 <= 1,000)
#
#
#
from collections import defaultdict

DIR = [0, (-1, 0), (1, 0), (0, -1), (0, 1)]
OPP_DIR = [0, 2, 1, 4, 3]
T = int(input())

for t in range(T):
    N, M, K = map(int, input().split())

    simul = {}
    total = 0
    for i in range(K):
        x, y, v, d = map(int, input().split())
        simul[(x, y)] = (v, d)
        total += v

    def get_next_pos(pos, d):
        return pos[0] + DIR[d][0], pos[1] + DIR[d][1]

    def is_in_drug(pos):
        return (pos[0] == 0 or pos[0] == N-1 or
                pos[1] == 0 or pos[1] == N-1)

    for i in range(M):
        queued_simul = defaultdict(list)

        for pos, info in simul.items():
            next_pos = get_next_pos(pos, info[1])
            if is_in_drug(next_pos):
                total -= info[0] - info[0] // 2
                info = (info[0] // 2, OPP_DIR[info[1]])
            queued_simul[next_pos].append(info)

        next_simul = {}
        for pos in queued_simul:
            pos_total = 0
            max_v = float('-inf')
            d = 0
            for info in queued_simul[pos]:
                if max_v < info[0]:
                    max_v = info[0]
                    d = info[1]
                pos_total += info[0]

            next_simul[pos] = (pos_total, d)
        simul = next_simul
    print(f"#{t+1}", total)
