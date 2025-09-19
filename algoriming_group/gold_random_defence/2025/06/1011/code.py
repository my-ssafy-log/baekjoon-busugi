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

"""
[(4D - 1) ^ 0.5]

[1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6]
1
1

2
1 1

3
1 1 1

4
1 2 1

5
1 2 1 1

6
1 2 2 1

7
1 2 2 1 1

8
1 2 2 2 1

9
1 2 3 2 1

10
1 2 3 2 1 1

11
1 2 3 2 2 1

12
1 2 3 3 2 1

13
"""