from typing import List

str1 = input()
str2 = input()

dp: List[List[int]] = []

for i in range(len(str1)+1):
    dp.append([])
    for j in range(len(str2)+1):
        if i == 0 or j == 0:
            dp[i].append(0)
        elif str1[i-1] == str2[j-1]:
            dp[i].append(dp[i-1][j-1] + 1)
        else:
            dp[i].append(max(dp[i-1][j], dp[i][j-1]))
print(dp[-1][-1])