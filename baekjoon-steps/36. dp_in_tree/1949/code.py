import sys
sys.setrecursionlimit(10000)

def readline():
    return sys.stdin.readline().rstrip()

N = int(readline())

arr = [0] + list(map(int, readline().split()))

tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, readline().split())
    tree[u].append(v)
    tree[v].append(u)

visited = [False] * (N+1)
memoized = [[None, None] for _ in range(N+1)]
def dfs(cur, is_selected):
    if memoized[cur][int(is_selected)] is not None:
        return memoized[cur][int(is_selected)]

    visited[cur] = True

    total = arr[cur] if is_selected else 0
    for child in tree[cur]:
        if visited[child]:
            continue
        max_val = 0
        if not is_selected:
            max_val = dfs(child, True)
        max_val = max(max_val, dfs(child, False))
        total += max_val
    # print(cur, is_selected, total)
    visited[cur] = False

    memoized[cur][int(is_selected)] = total
    return total

print(max(dfs(1, True),
          dfs(1, False)))
