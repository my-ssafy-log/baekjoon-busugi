n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from collections import deque
adj = [[] for _ in range(n+1)]

for edge in edges:
    a, b = edge
    adj[a].append(b)
    adj[b].append(a)

def check(start):
    queue = deque([(start, 1)])
    while queue:
        cur, color = queue.popleft()
        for nbr in adj[cur]:
            if box[nbr] == box[cur]:
                return False
            if box[nbr] != -1:
                continue

            box[nbr] = 1 - color
            queue.append((nbr, 1 - color))
    return True

box = [-1] * (n+1)
is_possible = True
for i in range(1, n+1):
    if box[i] != -1:
        continue
    box[i] = 1
    if not check(i):
        is_possible = False
        break

print(int(is_possible))

