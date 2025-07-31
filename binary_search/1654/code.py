import sys
import math

def readline():
    return sys.stdin.readline().rstrip()

K, N = map(int, readline().split())

arr = []

min_v = math.inf

for k in range(K):
    v = int(readline())
    arr.append(v)
    if min_v > v: min_v = v

s = 1
e = min_v * 2
max_len = 0
while s <= e:
    mid = (s + e) // 2
    # print('mid:', mid)
    is_big = False

    lan_number = 0
    for num in arr:
        lan_number += num // mid
        if lan_number >= N:
            is_big = True
            break
    if is_big:
        if max_len < mid:
            max_len = mid
        s = mid+1
    else:
        e = mid-1
print(max_len)