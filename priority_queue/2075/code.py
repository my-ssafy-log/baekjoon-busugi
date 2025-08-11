import heapq
import sys

def readline():
    return sys.stdin.readline().rstrip()

N = int(readline())

pq = list(map(int, readline().split()))
heapq.heapify(pq)

for i in range(N-1):
    row = list(map(int, readline().split()))
    for num in row:
        heapq.heappush(pq, num)
        heapq.heappop(pq)
print(sorted(pq)[0])