T = int(input())

for t in range(T):
    N, M, K = map(int, input().split())

    origin_map: dict[tuple[int, int], int] = {}
    simul_map = {}

    alive = 0

    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(M):
            if row[j] > 0:
                alive += 1
                origin_map[(i, j)] = row[j]
                simul_map[(i, j)] = row[j]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    next_simul_map = {}

    def bunsik(pos):
        global next_simul_map
        x, y = pos
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if (nx, ny) in simul_map: continue
            
            next_mic = max(next_simul_map.get((nx, ny), 0), origin_map[(x, y)])
            origin_map[(nx, ny)] = next_mic
            next_simul_map[(nx, ny)] = next_mic

    for _ in range(K):
        next_simul_map = simul_map.copy()
        for pos in simul_map:
            simul_map[pos] -= 1
            if simul_map[pos] == 0:
                bunsik(pos)
            elif simul_map[pos] == -origin_map[pos]:
                alive -= 1
        print("origin_map")
        print(origin_map)
        print("simul_map")
        print(simul_map)
        simul_map = next_simul_map