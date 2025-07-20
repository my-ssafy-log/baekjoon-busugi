n = int(input())

dp = [(0, 0)]

for i in range(1, n+1):
    v = int(input())
    
    if i == 1:
        dp.append((v, v))
    else:
        dp.append((
            v + dp[i-1][1],
            v + max(dp[i-2])
        ))
print(max(dp[-1]))