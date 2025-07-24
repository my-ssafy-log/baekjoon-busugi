n, k = map(int, input().split())

dp = [0] + [0] * k

for i in range(n):
    w, v = map(int, input().split())

    # print(f"#{i+1}")
    for j in range(k, w-1, -1):
        dp[j] = max(dp[j], v + dp[j-w])
        # print(dp)
print(max(dp))