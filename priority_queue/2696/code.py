
import sys
from heapq import heappush, heappop

sys.stdin = open('sample_input.txt')

def readline():
    return sys.stdin.readline().rstrip()

T = int(readline())

for t in range(T):
    M = int(readline())
    arr = [None]
    for i in range((M-1) // 10 + 1):
        arr.extend(list(map(int, readline().split())))

    res = []

    gte_hq = []  # 최소힙을 유지하는 pivot보다 크거나 같은 숫자들
    lt_hq = []  # 최대힙을 유지하는 pivot보다 작은 숫자들

    gte = 0
    lt = 0
    pivot = arr[1]
    for i in range(1, M+1):
        if i == 1:
            res.append(pivot)
            continue

        if arr[i] >= pivot:
            gte += 1
            heappush(gte_hq, arr[i])
        else:
            lt += 1
            heappush(lt_hq, -arr[i])

        if i % 2 == 1:
            if gte == lt:
                pass
            elif gte > lt:  # gte가 2, lt가 0일 때
                heappush(lt_hq, -pivot)
                pivot = heappop(gte_hq)
            else:  # gte가 0, lt가 2일 때
                heappush(gte_hq, pivot)
                pivot = -heappop(lt_hq)

            res.append(pivot)

            gte = 0
            lt = 0
    
    print(len(res))
    for i in range(0, len(res), 10):
        print(*res[i:i+10])