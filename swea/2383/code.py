import math
from collections import defaultdict

T = int(input())

for t in range(T):
    N = int(input())

    pos_list = []
    stairs_size_list = []
    stairs_list = [] # len: 2
    
    for i in range(N):
        row = list(map(int, input().split()))
        for j, cell in enumerate(row):
            if cell == 1:
                pos_list.append((i, j))
            if cell >= 2:
                stairs_size_list.append(cell)
                stairs_list.append((i, j))
    
    next_pos_list = []

    def get_next_pos(pos, stairs_index):
        x, y = pos
        gx, gy = stairs_list[stairs_index]

        # x를 우선적으로 계산함
        if gx < x or gx > x:
            x = x + int(math.copysign(1, gx - x))
        elif gy < y or gy > y:
            y = y + int(math.copysign(1, gy - y))
        
        if next_pos_list.count(pos) <= stairs_people_map[stairs_index]:
            return x, y
        
        # 만약 이미 이동하려는 누군가가 있다면
        # y를 우선적으로 다음 자리를 계산함
        if (x, y) in next_pos_list:
            x, y = pos
            if gy < y or gy > y:
                y = y + int(math.copysign(1, gy - y))

        return x, y
    
    # 계단에서 내려가고 있는 시간
    stairs_map = defaultdict(int)
    # 계단에 있는 사람 수
    stairs_people_map = defaultdict(int)
    # 이미 계단을 다 내려왔는가?
    visited = [False] * len(pos_list)

    def calc_next(sorted_pos_stairs_list):
        # print(sorted_pos_stairs_list, visited)
        for i, (pos, stairs_index) in enumerate(sorted_pos_stairs_list):
            if visited[i]: continue

            if pos == stairs_list[stairs_index] and stairs_people_map[stairs_index] < 3:
                stairs_map[i] += 1
                stairs_people_map[stairs_index] += 1
                if stairs_map[i] > stairs_size_list[stairs_index]:
                    visited[i] = True
                    stairs_people_map[stairs_index] -= 1
                continue

            next_pos = get_next_pos(
                pos, stairs_index)
            
            next_pos_list.append(next_pos)
            
            sorted_pos_stairs_list[i] = (next_pos, stairs_index)
    
    def compare(pos_stairs):
        pos, stairs_index = pos_stairs
        return abs(pos[0] - stairs_list[stairs_index][0]) + abs(pos[1] - stairs_list[stairs_index][1])
    
    min_time = math.inf

    def brute_force_stairs(pos_stairs_list, step):
        """
        완전탐색하는 함수입니다.
        Args:
            pos_stairs_list: list[(P좌표, 목적지)]
            step: pos_stairs_list 길이
        """
        
        global next_pos_list, min_time, visited, stairs_map, stairs_people_map
        if step == len(pos_list):
            stairs_map = defaultdict(int)
            visited = [False] * len(pos_list)
            sorted_pos_stairs_list = sorted(pos_stairs_list, key=compare)

            time = 0

            while not all(visited):
                next_pos_list = []
                stairs_people_map = defaultdict(int)
                calc_next(sorted_pos_stairs_list)
                time += 1

            min_time = min(min_time, time)
            # print("min_time", min_time)
            return
        
        brute_force_stairs(pos_stairs_list + [(pos_list[step], 0)], step + 1)
        brute_force_stairs(pos_stairs_list + [(pos_list[step], 1)], step + 1)

    brute_force_stairs([(pos_list[0], 0)], 1)
    brute_force_stairs([(pos_list[0], 1)], 1)
    print(f"#{t+1}", min_time)
