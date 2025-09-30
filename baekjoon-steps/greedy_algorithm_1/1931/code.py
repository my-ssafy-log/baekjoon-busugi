import sys

def readline():
    return sys.stdin.readline().rstrip()

N = int(readline())
arr = []

for _ in range(N):
    arr.append(
        tuple(map(int, readline().split()))
    )

arr.sort(key=lambda x: (x[1], x[0]))

# for time in arr:
#     print(time)

cnt = 0
finished_time = -1

for start, end in arr:
    if finished_time <= start:
        finished_time = end
        cnt += 1
print(cnt)