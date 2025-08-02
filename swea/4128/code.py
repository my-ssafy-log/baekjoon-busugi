from itertools import combinations
import math

T = int(input())

for t in range(T):
    N = int(input())
    matrix = []
    for n in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    comb_list = list(combinations([i for i in range(N)], N//2))
    comb_list_len = len(comb_list)
    a_group_list = comb_list[:comb_list_len//2]
    b_group_list = list(reversed(comb_list[comb_list_len//2:]))

    min_differnce = math.inf

    for i in range(comb_list_len//2):
        a_sum = 0
        a_pair_list = list(combinations(a_group_list[i], 2))
        for pair in a_pair_list:
            a_sum += matrix[pair[0]][pair[1]] + matrix[pair[1]][pair[0]]
        b_sum = 0
        b_pair_list = list(combinations(b_group_list[i], 2))
        for pair in b_pair_list:
            b_sum += matrix[pair[0]][pair[1]] + matrix[pair[1]][pair[0]]

        if min_differnce > abs(a_sum - b_sum):
            min_differnce = abs(a_sum - b_sum)
    print(f"#{t+1} {min_differnce}")