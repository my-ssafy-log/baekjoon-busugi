n = int(input())

arr = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    if i == 0:
        dp[i] = arr[i]
    else:
        dp[i] = max(arr[i] + dp[i-1], arr[i])
print(max(dp))