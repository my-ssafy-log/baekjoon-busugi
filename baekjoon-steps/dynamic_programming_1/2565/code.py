n = int(input())

input_arr = []
arr = [(0, 0)]
dp = [0]

for _ in range(n):
    cur_start, cur_end = map(int, input().split())
    input_arr.append((cur_start, cur_end))

input_arr.sort(key=lambda x: x[0])

for cur_start, cur_end in input_arr:
    len_arr = []
    for i, (start, end) in enumerate(arr):
        if (start < cur_start and end < cur_end):
            len_arr.append(dp[i])
    arr.append((cur_start, cur_end))
    dp.append(max(len_arr) + 1)
print(n - max(dp))