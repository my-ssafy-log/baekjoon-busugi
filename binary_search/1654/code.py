import sys
import math

def readline():
    return sys.stdin.readline().rstrip()

K, N = map(int, readline().split())

arr = []

max_len = -math.inf

for k in range(K):
    v = int(readline())
    arr.append(v)
    if max_len < v: max_len = v

s = 0
e = max_len * 2
min_n = math.inf
max_v = 0

def get_lan_cable(arr, mid):
    return sum([(num//mid) for num in arr])

while s < e:
    # print(s, e)
    mid = (s+e) // 2
    lan_cable = get_lan_cable(arr, mid)

    if lan_cable >= N:
        min_n = min(min_n, lan_cable)
        max_v = max(max_v, mid)
        s = mid + 1
    else:
        e = mid
print(max_v)