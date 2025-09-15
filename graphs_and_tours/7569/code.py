import sys
sys.stdin = open('graphs_and_tours/7569/sample_input.txt')

M, N, H = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

empty_cnt = 0
queue = []
for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 1:
                queue.append((x, y, z))
            elif box[z][y][x] == 0:
                empty_cnt += 1

def out_of_range(x, y, z):
    return not (0 <= x < M and 0 <= y < N and 0 <= z < H)

time = 0
while queue:
    new_queue = []

    while queue:
        x, y, z = queue.pop()
        for dx, dy, dz in [(0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0)]:
            nx, ny, nz = x + dx, y + dy, z + dz
            if out_of_range(nx, ny, nz):
                continue
            if box[nz][ny][nx] == 0:
                empty_cnt -= 1
                box[nz][ny][nx] = 1
                new_queue.append((nx, ny, nz))
    
    if new_queue:
        time += 1
        queue = new_queue

if empty_cnt == 0:
    print(time)
else:
    print(-1)
