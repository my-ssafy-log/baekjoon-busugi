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
    total_set = {cur} if is_selected else set()
    for child in tree[cur]:
        if visited[child]:
            continue
        max_val = 0
        max_set = set()

        if not is_selected:
            max_val, max_set = dfs(child, True)

        if dfs(child, False)[0] > max_val:
            max_val, max_set = dfs(child, False)
        total += max_val
        total_set |= max_set
    visited[cur] = False

    memoized[cur][int(is_selected)] = (total, total_set)
    return total, total_set

case1 = dfs(1, True)
case2 = dfs(1, False)
max_case = case1 if case1[0] > case2[0] else case2
print(max_case[0])
print(*sorted(max_case[1]))
