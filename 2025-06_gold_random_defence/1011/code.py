import math
import sys

def readline():
    # return input()
    return sys.stdin.readline().rstrip()

T = int(readline())

for t in range(T):
    x, y = map(int, readline().split())

    t = 0
    k = 1
    d = y - x
    while True:
        # print(k, end=' ')
        d -= k
        t += 1
        if d == 0: break
        if d >= (k+1) * (k+2) // 2:
            k += 1
        elif d >= k * (k+1) // 2:
            pass
        else:
            k -= 1
    print(t)