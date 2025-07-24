n, m = map(int, input().split())
pre_sum = [0] + list(map(int, input().split()))

for i in range(2, n+1):
    pre_sum[i] += pre_sum[i-1]

for _ in range(m):
    i, j = map(int, input().split())

    print(pre_sum[j] - pre_sum[i-1])