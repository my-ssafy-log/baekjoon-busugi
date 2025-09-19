import sys
sys.stdin = open('gold_random_defence/2025/04/1241/sample_input.txt')

import sys

def readline():
    return sys.stdin.readline().rstrip()

N = int(readline())

count = [0] * (int(1e6) + 1)

arr = [int(readline()) for _ in range(N)]

for v in arr:
    count[v] += 1

for v in arr:
    sqrt = int(v ** (1/2))

    if sqrt ** 2 == v:  # 제곱수라면
        cnt = -count[sqrt]
    else:
        cnt = 0
    
    for divisor in range(1, int(v ** (1/2)) + 1):
        if v % divisor == 0:
            cnt += count[divisor] + count[v // divisor]
    print(cnt - 1)  # 자기 자신 하나는 뺌
