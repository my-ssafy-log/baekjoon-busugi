n = int(input())

dp = [1] * 10
temp = []

for i in range(n-1):
    for j in range(10):
        # 양 끝이면 바깥쪽 제외, 안쪽에 있는 계단 수만 더함
        if j == 0:
            temp.append(dp[1] % 1000000000)
        elif j == 9:
            temp.append(dp[8] % 1000000000)
        else:
            temp.append((dp[j-1] + dp[j+1]) % 1000000000)
    dp = temp
    temp = []
print(sum(dp[1:]) % 1000000000)