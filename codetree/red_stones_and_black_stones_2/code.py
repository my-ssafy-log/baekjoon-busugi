C, N = map(int, input().split())
T = [int(input()) for _ in range(C)]
AB = [tuple(map(int, input().split())) for _ in range(N)]
A = [ab[0] for ab in AB]
B = [ab[1] for ab in AB]

# Please write your code here.
import heapq

T.sort()
AB.sort()

i = 0
cnt = 0

hq = []

for t in T:
    while i < len(AB) and AB[i][0] <= t:
        A, B = AB[i]
        heapq.heappush(hq, (B, A))
        i += 1
    ans = None
    while hq:
        if hq[0][0] >= t:
            ans = heapq.heappop(hq)
            break
        heapq.heappop(hq)
    if ans is not None:
        cnt += 1
print(cnt)
