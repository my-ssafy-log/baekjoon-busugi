n, k = map(int, input().split())
units = list(filter(lambda x: x <= k,[int(input()) for _ in range(n)]))
units.sort()

dp = [0] * (k+1)
dp[0] = 1

for unit in units:
    for i in range(unit, k+1):
        dp[i] += dp[i-unit]
print(dp[k])