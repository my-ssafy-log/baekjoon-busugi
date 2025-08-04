import sys
import math

def readline():
    return sys.stdin.readline().rstrip()

N, M = map(int, readline().split())

trees = list(map(int, readline().split()))

s = 0
e = max(trees)

max_height = 0

while s <= e:
    mid = (s+e) // 2

    amount = 0
    for tree in trees:
        amount += max(tree - mid, 0)
    if amount < M:
        e = mid - 1
    else:
        s = mid + 1
        max_height = max(max_height, mid)
print(max_height)