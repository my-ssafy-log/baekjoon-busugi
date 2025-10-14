import sys

INF = float('inf')

def readline():
    return sys.stdin.readline().rstrip()

n = int(readline())
m = int(readline())

d = [[INF] * (n+1) for _ in range(n+1)]
paths = [
    [
        [] for _ in range(n+1)
    ] for _ in range(n+1)
]

for i in range(n+1): d[i][i] = 0

for _ in range(m):
    a, b, c = map(int, readline().split())
    d[a][b] = min(d[a][b], c)
    paths[a][b] = [a, b]

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            nxt_dist = d[i][k] + d[k][j]
            if d[i][j] > nxt_dist:
                d[i][j] = nxt_dist
                paths[i][j] = [*paths[i][k][:-1], k, *paths[k][j][1:]]

print(
    *(
        ' '.join(
            map(lambda x: str(x if x != INF else 0),
                dist[1:])) for dist in d[1:]
    ),
    sep='\n')

paths_ans = (
    ' '.join(map(str, [len(goal_path)] + goal_path)) if goal_path else 0
                                for path in paths[1:]
                                    for goal_path in path[1:])
print(*paths_ans, sep='\n')
