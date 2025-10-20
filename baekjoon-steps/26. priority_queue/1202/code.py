import sys
# ! 주석 처리해야함
sys.stdin = open('priority_queue/1202/sample_input.txt')

import sys
from collections import namedtuple
from heapq import heappush, heappop

Gem = namedtuple('Gem', 'weight, value')

def readline():
    return sys.stdin.readline().rstrip()

N, K = map(int, readline().split())

gems = [Gem(*map(int, readline().split())) for _ in range(N)]
backpacks = [int(readline()) for _ in range(K)]
gems.sort(key=lambda gem: gem.weight)
backpacks.sort()

total = 0
idx = 0  # 현재 추가할 보석 위치
value_hq = []
for backpack in backpacks:
    # backpack 용량보다 작은 보석 무게들을 가치 기준 최대힙에 넣음
    while idx < len(gems) and gems[idx].weight <= backpack:
        heappush(value_hq, -gems[idx].value)
        idx += 1
    
    # 가치 기준 최대힙에서 하나 뽑아옴
    if value_hq:
        max_value_gem = heappop(value_hq)
        total += -max_value_gem  # total에 더함

print(total)
