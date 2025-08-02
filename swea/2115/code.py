from itertools import combinations

T = int(input())

for t in range(T):
    N, M, C = map(int, input().split())

    board = []

    for _ in range(N):
        row = list(map(int, input().split()))
        board.append(row)
    
    def get_max_from_barrels(arr, size):
        arr_len = len(arr)
        comb_list = []
        max_v = 0

        for n in range(arr_len, 0, -1):
            comb_list.extend(list(combinations(arr, n)))
        
        for comb in comb_list:
            if sum(comb) <= size:
                sqrd_sum = sum(map(lambda x: x**2, comb))
                if max_v < sqrd_sum: max_v = sqrd_sum
        return max_v
    
    max_v = 0

    for i1 in range(N):
        for j1 in range(N-M+1):

            for i2 in range(i1, N):
                for j2 in range(N-M+1):
                    if i1 == i2 and j1+M-1 >= j2:
                        continue
                    if j2+M-1 >= N:
                        continue
                        
                    # print(f"i1: {i1}, j1: {j1}")
                    # print(f"i2: {i2}, j2: {j2}")
                    # print()

                    max1 = get_max_from_barrels(board[i1][j1:j1+M], C)
                    max2 = get_max_from_barrels(board[i2][j2:j2+M], C)

                    if (max_v < max1 + max2): max_v = max1 + max2
    print(f"{t+1} {max_v}")