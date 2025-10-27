import sys

def readline():
    return sys.stdin.readline().rstrip()

N = int(readline())

tree = [[] for _ in range(N+1)]
subtree_cnts = [0] * (N+1)
results = [0] * (N+1)

for _ in range(N-1):
    u, v, d = map(int, readline().split())
    tree[u].append((v, d))
    tree[v].append((u, d))

visited = [False] * (N+1)
def dfs(root):
    visited[root] = True
    total_d = 0

    stack = [(root, False)]

    while stack:
        root, processed = stack.pop()

        if processed:
            subtree_cnts[root] = 1
            total_d = 0

            for nbr, nbr_d in tree[root]:
                total_d += results[nbr] + nbr_d * subtree_cnts[nbr]
                subtree_cnts[root] += subtree_cnts[nbr]
            results[root] = total_d
        else:
            stack.append((root, True))
            visited[root] = True
            for nbr, nbr_d in tree[root]:
                if visited[nbr]:
                    continue
                stack.append((nbr, False))

dfs(1)

visited = [False] * (N+1)
def find(root):
    stack = [root]
    while stack:
        root = stack.pop()
        visited[root] = True

        for nbr, nbr_d in tree[root]:
            if visited[nbr]:
                continue
            results[nbr] = results[root] - (subtree_cnts[nbr] * nbr_d) + (N - subtree_cnts[nbr]) * nbr_d
            stack.append(nbr)

find(1)
# print(subtree_cnts)
print(*results[1:], sep='\n')
