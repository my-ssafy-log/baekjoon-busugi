import math
T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    min_v = math.inf
    for i in range(0, len(arr)-K+1):
        min_v = min(min_v, arr[i+K-1] - arr[i])
    print(f"#{t+1} {min_v}")
