from collections import deque

INF = float('inf')
T = int(input())

for t in range(T):
    A, B = map(int, input().split())
    d = [-1] * 10000
    recnstr_command = [None] * 10000
    d[A] = 0
    queue = deque([A])

    def shift_left(value):
        return value * 10 % 10000 + value // 1000

    def shift_right(value):
        return value // 10 + (value % 10) * 1000

    while queue:
        cur = queue.popleft()

        if cur == B:
            break

        nxt_dist = d[cur] + 1

        if d[cur * 2 % 10000] == -1:
            d[cur * 2 % 10000] = nxt_dist
            recnstr_command[cur * 2 % 10000] = ('D', cur)
            queue.append(cur * 2 % 10000)
        if d[(cur-1) % 10000] == -1:
            d[(cur-1) % 10000] = nxt_dist
            recnstr_command[(cur-1) % 10000] = ('S', cur)
            queue.append((cur-1) % 10000)
        if d[shift_left(cur)] == -1:
            d[shift_left(cur)] = nxt_dist
            recnstr_command[shift_left(cur)] = ('L', cur)
            queue.append(shift_left(cur))
        if d[shift_right(cur)] == -1:
            d[shift_right(cur)] = nxt_dist
            recnstr_command[shift_right(cur)] = ('R', cur)
            queue.append(shift_right(cur))

    cur_cmd = B
    path = []
    while recnstr_command[cur_cmd] is not None:
        path.append(recnstr_command[cur_cmd][0])
        cur_cmd = recnstr_command[cur_cmd][1]
    print(*reversed(path), sep='')
