import sys
import math

def readline():
    return sys.stdin.readline().rstrip()

def get_dist(pos_a, pos_b):
    return math.sqrt(pow(pos_a[0] - pos_b[0], 2) + pow(pos_a[1] - pos_b[1], 2))

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union_set(a, b):
    pa = find_set(a)
    pb = find_set(b)

    if rank[pb] < rank[pa]:
        p[pb] = pa
    elif rank[pa] < rank[pb]:
        p[pa] = pb
    else:
        p[pb] = pa
        rank[pa] += 1

N, M = map(int, readline().split())

p = list(range(N+1))
rank = [0] * (N+1)

pos_list = [tuple(map(int, readline().split())) for _ in range(N)]
edges = []

for i in range(N-1):
    pos_a = pos_list[i]
    for j in range(i+1, N):
        pos_b = pos_list[j]
        # n번째 위치로
        edges.append((i+1, j+1, get_dist(pos_a, pos_b)))

edges.sort(key=lambda edge: edge[2])

total_weight = 0
for _ in range(M):
    u, v = map(int, input().split())
    union_set(u, v)


for edge in edges:
    a, b, w = edge
    if find_set(a) != find_set(b):
        union_set(a, b)
        total_weight += w
total_weight *= 1000
print('%.2f' % (round(total_weight, -1) / 1000))
