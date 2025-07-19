import math

n = int(input())

arr = list(map(int, input().split()))
prefix_sum = [arr[0]]

for i in range(1, n):
    prefix_sum.append(
        prefix_sum[i-1]
        + arr[i]
    )

max_v = -math.inf

for i in range(-1, n-1):
    for j in range(i+1, n):
        if i < 0:
            max_v = max(prefix_sum[j], max_v)
        else:
            max_v = max(prefix_sum[j] - prefix_sum[i], max_v)
print(max_v)