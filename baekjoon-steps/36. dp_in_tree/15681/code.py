import sys
sys.setrecursionlimit(100000)

def readline():
    return sys.stdin.readline().rstrip()

N, R, Q = map(int, readline().split())

adj = {i: [] for i in range(N+1)}
for _ in range(N-1):
    U, V = map(int, readline().split())
    adj[U].append(V)
    adj[V].append(U)

queries = [int(readline()) for _ in range(Q)]

subtree_numbers = [0] * (N+1)

visited = [False] * (N+1)
def find_subtree_number(root):
    visited[root] = True
    cnt = 1
    for child in adj[root]:
        if visited[child]:
            continue
        cnt += find_subtree_number(child)
    subtree_numbers[root] = cnt
    return cnt

find_subtree_number(R)
print(*[subtree_numbers[query] for query in queries], sep='\n')
