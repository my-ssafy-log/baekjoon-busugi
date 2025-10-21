dp = [0, 1, 1, 1, 2, 2]

t = int(input())
for test_case in range(t):
    n = int(input())
    for i in range(len(dp), n+1):
        dp.append(dp[i - 1] + dp[i - 5])

    print(dp[n])