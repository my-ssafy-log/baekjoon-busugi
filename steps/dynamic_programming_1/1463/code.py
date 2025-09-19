n = int(input())

dp = [0] * n + [0]

cnt = n

for i in range(1, n+1):
    if i*2 <= n and (dp[i*2] == 0 or dp[i*2] > dp[i] + 1):
        dp[i*2] = dp[i] + 1
    if i*3 <= n and (dp[i*3] == 0 or dp[i*3] > dp[i] + 1):
        dp[i*3] = dp[i] + 1
    if i+1 <= n and (dp[i+1] == 0 or dp[i+1] > dp[i] + 1):
        dp[i+1] = dp[i] + 1
print(dp[n])