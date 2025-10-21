from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

dp = [-10**9-1]
d = [0] * N
for i, v in enumerate(arr):
    length = bisect_left(dp, v)
    if len(dp) == length:
        dp.append(v)
    else:
        dp[length] = v
    d[i] = length

max_idx = d.index(max(d))
path = [arr[max_idx]]
cur_idx = max_idx
for idx in range(max_idx, -1, -1):
    if d[idx] == d[cur_idx] - 1:
        cur_idx = idx
        path.append(arr[idx])

print(len(path))
print(*path[::-1])
