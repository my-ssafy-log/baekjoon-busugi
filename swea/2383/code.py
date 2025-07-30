from typing import Tuple
T = int(input())

for t in range(T):
    N = int(input())

    pos_list = []
    stairs_number_list = []
    stairs_list = []
    
    for i in range(N):
        row = list(map(int, input().split()))
        for j, cell in enumerate(row):
            if cell == 1:
                pos_list.append((i, j))
            if cell >= 2:
                stairs_number_list.append(cell)
                stairs_list.append((i, j))
    
    def get_dist(A: Tuple[int, int], B: Tuple[int, int]):
        return abs(A[0] - B[0]) + abs(A[1] - B[1])
    
    def brute_force_stairs(stairs_orders, step):
        if step == N:
            stairs_distances = [
                [],
                []
            ]
            
            for i, stairs_order in enumerate(stairs_orders):
                stairs_distances[stairs_order].append(
                    get_dist(stairs_list[stairs_order], pos_list[i])
                )

            stairs_distances[0].sort()
            stairs_distances[1].sort()
            print(stairs_distances[0])
            print(stairs_distances[1])

            spend_time = 0
            # 계단에 있는 사람 수
            first_stairs_people_number = 0
            second_stairs_people_number = 0
            t = 0

            while True:
                t += 1

                first_stairs_distances = stairs_distances[0]

                for i in range(len(first_stairs_distances)):
                    if (first_stairs_distances[i] - 1 == 0 and
                        first_stairs_people_number < stairs_number_list[0]):
                        pass
                    
                    first_stairs_distances[i] -= 1
                    if first_stairs_distances[i] == 0:
                        first_stairs_people_number += 1
                
            return
        
        brute_force_stairs(stairs_orders + [0], step + 1)
        brute_force_stairs(stairs_orders + [1], step + 1)
        pass
    brute_force_stairs([0], 1)
    brute_force_stairs([1], 1)