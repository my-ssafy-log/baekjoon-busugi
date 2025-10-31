from collections import defaultdict, deque

N, L = map(int, input().split())
arr = list(map(int, input().split()))

cnts = defaultdict(int)
dq = deque()
res = [0] * N

for i, v in enumerate(arr):
    cnts[v] += 1
    
    while dq and dq[-1][0] >= v:
        dq.pop()
    dq.append((v, i))

    if i >= L and dq[0][1] == i - L:
        dq.popleft()

    res[i] = dq[0][0]
print(*res)
