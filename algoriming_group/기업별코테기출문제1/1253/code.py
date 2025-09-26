import sys

def readline():
    return sys.stdin.readline().rstrip()

N = int(readline())
arr = list(map(int, readline().split()))
arr.sort()

cnt = 0
for i in range(N):
    found = False
    s, e = 0, N-1
    
    if s == i:
        s += 1
    if e == i:
        e -= 1

    cur = arr[i]

    while True:
        if s >= e:
            break
        s_plus_e = arr[s] + arr[e]
        if s_plus_e < cur:
            s += 1
        elif s_plus_e > cur:
            e -= 1
        else:
            found = True
            break
        if s == i:
            s += 1
        if e == i:
            e -= 1

    if found:
        cnt += 1
print(cnt)
