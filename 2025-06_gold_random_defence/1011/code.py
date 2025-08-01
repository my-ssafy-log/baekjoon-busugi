import math
import sys

def readline():
    return sys.stdin.readline().rstrip()

T = int(readline())

for t in range(T):
    x, y = map(int, readline().split())

    min_step = math.inf

    def f(k, d, step):
        global min_step
        if d < 0: return None
        if d == 0:
            if k == 1:
                min_step = min(min_step, step)
            return None
        if k - 1 >= 1:
            f(k-1, d - (k-1), step + 1)
        if k >= 1: f(k, d-k, step + 1)
        f(k+1, d - (k+1), step + 1)
    f(0, y-x, 0)
    print(min_step)