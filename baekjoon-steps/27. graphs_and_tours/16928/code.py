from collections import deque

N, M = map(int, input().split())
ladder = [-1] * 101
snake = [-1] * 101
for i in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
for i in range(M):
    u, v = map(int, input().split())
    snake[u] = v

t = 0
queue = deque([1])

while True:
    done = False
    new_queue = deque()
    while queue:
        start = queue.popleft()
        if start >= 100:
            done = True
            break

        max_cells = [True] * 7
        for i in range(1, 7):
            if start + i <= 100 and ladder[start + i] != -1:
                max_cells[i] = False
                new_queue.append(ladder[start + i])
        for i in range(1, 7):
            if start + i <= 100 and snake[start + i] != -1:
                max_cells[i] = False
                new_queue.append(snake[start + i])

        max_cell = None
        for i in range(6, 0, -1):
            if max_cells[i]:
                max_cell = i
                break
        if max_cell is not None:
            new_queue.append(start + max_cell)

    if done:
        break

    queue = new_queue
    # print(new_queue)
    t += 1
print(t)