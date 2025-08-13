import sys
# from time import time

sys.stdin = open('sample_input.txt', 'r')

#
# 홈방범 서비스 운영비용은 크기 K가 커질수록 커진다.
# K는 중심에서의 길이, 운영 비용은 K * K + (K-1) * (K-1)
# 서비스 제공할 때 외곽으로 벗어나도 비용은 바뀌지 않음
#
# 홈방범 서비스 제공받는 집들은 각각 M의 비용을 지불함 (모든 집이 똑같이 M)
# 보안회사에서 손해를 보지 않는 한 최대한 많은 집에 홈방범 서비스를 제공하려고 함
# 도시 크기 N (5 <= N <= 20), 집마다 주는 비용 M
# N x N
# 집 개수 1 이상
# 보안회사가 서비스 제공하는데 받는비용-운영비용이 0이상이면서 서비스할 수 있는 최대한 많은 집의 수
#
#

# start_time = time()
T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    def get_ranges(x, y, K):
        ranges = []
        # 방범 범위를 절반을 나눴을 때 중심 부분 포함 윗부분
        for i in range(K):
            for j in range(-i, 1 + i):
                nx = x - K + 1 + i
                ny = j + y
                if not (0 <= nx < N and 0 <= ny < N):
                    continue
                ranges.append((nx, ny))

        for i in range(K-2, -1, -1):
            for j in range(-i, 1 + i):
                nx = x + K - 1 - i
                ny = j + y
                if not (0 <= nx < N and 0 <= ny < N):
                    continue
                ranges.append((nx, ny))

        return ranges

    max_houses = float('-inf')
    for K in range(1, N*2):
        for i in range(N):
            for j in range(N):
                cnt = 0
                ranges = get_ranges(i, j, K)

                for pos in ranges:
                    if matrix[pos[0]][pos[1]] == 1:
                        cnt += 1
                price = K * K + (K-1) * (K-1)
                if cnt * M - price >= 0:
                    max_houses = max(max_houses, cnt)
    print(f"#{t+1}", max_houses)

# end_time = time()
# print(end_time - start_time)
