from collections import defaultdict

N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
total_cost = sum(costs)

apps = zip(memories, costs)
table = [[0] * (total_cost+1) for _ in range(N+1)]
for i, app in enumerate(apps, 1):
    memory, cost = app
    for j in range(total_cost+1):
        if j < cost:
            table[i][j] = table[i-1][j]
        else:
            table[i][j] = max(table[i-1][j], memory + table[i-1][j-cost])

ans = None
for cost, mem in enumerate(table[N]):
    if mem >= M:
        ans = cost
        break

# pprint(table)
print(ans)