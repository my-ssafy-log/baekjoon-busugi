import sys
sys.stdin = open('algoriming_group/기업별코테기출문제1/1806/sample_input.txt')

import sys

def readline():
    return sys.stdin.readline().rstrip()

N, S = map(int, readline().split())
arr = list(map(int, readline().split()))
i = j = 0
part_sum = arr[0]

min_len = float('inf')
while i <= j and j < N:
    # print(i, j)
    if part_sum < S:
        j += 1

        if j < N:
            part_sum += arr[j]
    else:
        min_len = min(min_len, j - i + 1)
        part_sum -= arr[i]
        i += 1
if min_len == float('inf'):
    print(0)
else:
    print(min_len)
