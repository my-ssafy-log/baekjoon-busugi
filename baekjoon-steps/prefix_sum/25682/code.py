import math

N, M, K = map(int, input().split())

black_presum = [
    [0] * (M+1)
]
white_presum = [
    [0] * (M+1)
]

b_start_flag = 'B'

def calc_flag(i, j):
    global b_start_flag
    b_start_flag = 'B' if (i + j) % 2 == 0 else 'W'

for i in range(1, N+1):
    black_presum_arr = [0]
    white_presum_arr = [0]
    row = [0] + list(input())
    
    for j, cell in enumerate(row[1:], 1):
        calc_flag(i, j)
        black_presum_arr.append(
            black_presum_arr[j-1] +
            black_presum[i-1][j] - 
            black_presum[i-1][j-1] +
            (0 if cell == b_start_flag else 1)
        )
        white_presum_arr.append(
            white_presum_arr[j-1] +
            white_presum[i-1][j] - 
            white_presum[i-1][j-1] +
            (0 if cell != b_start_flag else 1)
        )
        # print(b_start_flag)
    black_presum.append(black_presum_arr)
    white_presum.append(white_presum_arr)

min_v = math.inf
for i in range(K, N+1):
    for j in range(K, M+1):
        black_partialsum = (black_presum[i][j] -
        black_presum[i][j-K] -
        black_presum[i-K][j] +
        black_presum[i-K][j-K])
        
        white_partialsum = (white_presum[i][j] -
        white_presum[i][j-K] -
        white_presum[i-K][j] +
        white_presum[i-K][j-K])

        min_v = min(min_v, min(black_partialsum, white_partialsum))
print(min_v)
# print("Black Start Presum")
# for row in black_presum:
#     print(row)
# print("White Start Presum")
# for row in white_presum:
#     print(row)
    