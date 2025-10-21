import sys;sys.stdin = open('input.txt')

import sys
from collections import defaultdict

def readline():
    return sys.stdin.readline().rstrip()

T = int(readline())

def find_set(x):
    if x in p and p[x] != x:
        p[x] = find_set(p[x])
    else:
        p[x] = x
    return p[x]

def union_set(a, b):
    pa = find_set(a)
    pb = find_set(b)
    if pa == pb:
        return

    if rank[pb] < rank[pa]:
        p[pb] = pa
        nums[pa] += nums[pb]
    elif rank[pa] < rank[pb]:
        p[pa] = pb
        nums[pb] += nums[pa]
    else:
        p[pb] = pa
        nums[pa] += nums[pb]
        rank[pa] += 1

for t in range(T):
    F = int(input())
    p = dict()
    rank = defaultdict(lambda: 1)
    nums = defaultdict(lambda: 1)
    relationships = [readline().split() for _ in range(F)]
    results = []
    for friend_a, friend_b in relationships:
        if find_set(friend_a) != find_set(friend_b):
            union_set(friend_a, friend_b)

        results.append(nums[find_set(friend_a)])
    print(*results, sep='\n')
