n = int(input())

arr = []

for i in range(n):

    arr.append(int(input()))

dp = [0, 0, arr[0], arr[0]]

for v in arr[1:]:

    a = v + dp[-1]

    b = v + max(dp[:-2])

    dp.append(a)

    dp.append(b)

# for v in dp:

#     print(v)

print(max(dp))

"""

4 3 1 0 1 2

0 4 7 4 5 8 8

0 4 3 5 7 6 9

2 4 3

"""