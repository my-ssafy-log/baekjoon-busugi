import sys
from collections import deque
from heapq import heappop, heappush

def readline():
    return sys.stdin.readline().rstrip()

N = int(readline())

tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, readline().split())
    tree[u].append(v)
    tree[v].append(u)

def find_leaves(root):
    parents = [None] * (N+1)
    visited = [False] * (N+1)
    leaves = []
    queue = deque([(root, 0)])

    while queue:
        cur, depth = queue.popleft()
        visited[cur] = True
        is_leaf = True
        for child in tree[cur]:
            if visited[child]:
                continue
            is_leaf = False
            parents[child] = cur
            queue.append((child, depth + 1))
        if is_leaf:
            heappush(leaves, (-depth, cur))
    return leaves, parents

leaves, parents = find_leaves(1)

queue = leaves[:]
mvc = set()
while queue:
    depth, leaf = heappop(queue)
    if leaf in mvc:
        continue
    parent = parents[leaf]
    
    if parent is None or parent in mvc:
        continue

    mvc.add(parent)
    grand_parent = parents[parent]
    if grand_parent is not None:
        heappush(queue, (depth + 2, grand_parent))

print(len(mvc))
