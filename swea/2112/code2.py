import sys

sys.stdin = open('sample_input.txt', 'r')

#
# 두깨 D
# 너비 W
# 세로방향에 대해서 동일한 셀들이 연속적으로 K개 있어야 한다. 이를 성능 검사 통과라고 한다.
# 이때 임의의 행의 특성을 하나로 통일시킬 수 있는데, 이를 약품 투입이라고 한다면
# 성능검사를 통과하는 최소 약품 투입 횟수를 구해야한다.
#
# ### 입력
# 테케 50
# D (3 <= 3 <= 13)
# W (1 <= W <= 20)
# K (1 <= K <= D)
# 특성은 A, B, 이렇게 2개
#
#


def test(matrix):
    for i in range(W):
        prev = matrix[0][i]
        cnt = 1
        for j in range(1, D):
            if prev == matrix[j][i]:
                cnt += 1
            else:
                prev = matrix[j][i]
                cnt = 1
            if cnt == K:
                break
        if cnt < K:
            return False
    return True


T = int(input())

for t in range(T):
    D, W, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(D)]
    origin_matrix = list(map(lambda arr: list(arr), matrix))

    if K == 1 or test(matrix):
        print(f"#{t+1}", 0)
        continue

    ok = False
    min_d = None

    def dfs(step, ni=0):
        global ok, min_d
        if step == d:
            ok = test(matrix)
            if ok:
                min_d = d
            return

        for i in range(ni, D):
            for drug in [0, 1]:
                if ok:
                    return ok
                matrix[i] = [drug] * W
                dfs(step + 1, i+1)
                matrix[i] = origin_matrix[i]

    for d in range(1, K+1):
        if ok:
            break
        dfs(0)

    print(f"#{t+1}", min_d)
