from typing import Tuple
T = int(input())

for t in range(T):
    N = int(input())

    pos_list = []
    stairs_list = []
    
    for i in range(N):
        row = list(map(int, input().split()))
        for j, cell in enumerate(row):
            if cell == 1:
                pos_list.append((i, j))
            if cell >= 2:
                stairs_list.append((i, j))
    
    def get_dist(A: Tuple[int, int], B: Tuple[int, int]):
        return abs(A[0] - B[0]) + abs(A[1] - B[1])
    
    def f(stairs_orders, step):
        if step == N:
            first_stairs_distance_list = []
            second_stairs_distance_list = []
            
            for i, stairs_order in enumerate(stairs_orders):
                if stairs_order == 0:
                    first_stairs_distance_list.append(
                        get_dist(stairs_list[0], pos_list[i])
                    )
                else:
                    second_stairs_distance_list.append(
                        get_dist(stairs_list[1], pos_list[i])
                    )
            first_stairs_distance_list.sort()
            second_stairs_distance_list.sort()
            print(stairs_orders)
            print(first_stairs_distance_list)
            print(second_stairs_distance_list)

            spend_time = 0
            first_stairs_queue = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
            second_stairs_queue = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]

            i = 0
            j = 0

            while True:
                min_t = min(first_stairs_distance_list[i], second_stairs_distance_list[j])
                spend_time += min_t
                pass
            return
        f(stairs_orders + [0], step + 1)
        f(stairs_orders + [1], step + 1)
        pass
    f([0], 1)
    f([1], 1)