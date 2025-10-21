import sys;
sys.setrecursionlimit(100000)

import math

N, M, K = map(int, input().split())

arr = [0] + [int(input()) for _ in range(N)]
tree = {}

def init(idx, start, end):
    if start == end:
        tree[idx] = arr[start]
        return

    mid = (start + end) // 2
    init(idx * 2, start, mid)
    init(idx * 2 + 1, mid+1, end)
    tree[idx] = tree[idx * 2] * tree[idx * 2 + 1] % (10**9 + 7)

init(1, 1, N)

def update(pos, v, start, end, idx):
    if not start <= pos <= end:
        return
    if start == end:
        tree[idx] = v
        return
    
    mid = (start + end) // 2
    update(pos, v, start, mid, idx * 2)
    update(pos, v, mid + 1, end, idx * 2 + 1)
    tree[idx] = tree[idx * 2] * tree[idx * 2 + 1] % (10**9 + 7)

def find(left, right, start, end, idx):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[idx]

    mid = (start + end) // 2
    a = find(left, right, start, mid, idx * 2)
    b = find(left, right, mid + 1, end, idx * 2 + 1)
    return a * b % (10**9 + 7)

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:
        update(b, c, 1, N, 1)
    if a == 2:
        res = find(b, c, 1, N, 1)
        print(res)
