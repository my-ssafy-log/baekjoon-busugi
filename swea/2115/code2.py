import sys

sys.stdin = open('sample_input.txt', 'r')

#
# N x N (3 <= N <= 10)
# 꿀을 채취할 수 있는 벌통 수 M
# 벌통을 가로로 연속적으로 붙어있는 벌통에서만 채취가능
# 두 일꾼을 벌꿀을 채취할 수 있는 최대치 C가 주어지는데,
# 이 C를 넘어서 벌꿀을 채취할 수 없다.
# 수익은 채취한 벌꿀의 양의 제곱 후의 합이다.
# 두 일꾼이 A, B, C 를 채취했다면 A^2 + B^2 + C^2이 수익이 됨
#
# ### 입력
# 테케
# N, M, C
# N x N의 2차원 배열
#

T = int(input())

for t in range(T):
    N, M, C = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_v = float('-inf')
    # 일꾼A 채취 위치 (i1, j1)
    for i1 in range(N):
        for j1 in range(N-M+1):

            # 일꾼B 채취 위치 (i2, j2)
            for i2 in range(i1, N):
                for j2 in range(N-M+1):
                    if i1 == i2:
                        if j1 + M - 1 >= j2:
                            continue
                    a_honeys = matrix[i1][j1:j1+M]
                    b_honeys = matrix[i2][j2:j2+M]

                    dp = [0] * (C+1)
                    for honey in a_honeys:
                        for i in range(C, honey-1, -1):
                            if dp[i] < dp[i-honey] + honey ** 2:
                                dp[i] = dp[i-honey] + honey ** 2
                    a_max = max(dp)

                    dp = [0] * (C + 1)
                    for honey in b_honeys:
                        for i in range(C, honey - 1, -1):
                            if dp[i] < dp[i - honey] + honey ** 2:
                                dp[i] = dp[i - honey] + honey ** 2
                    b_max = max(dp)

                    max_v = max(max_v, a_max + b_max)
    print(f"#{t+1}", max_v)
