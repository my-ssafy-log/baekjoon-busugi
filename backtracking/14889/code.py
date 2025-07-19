import math
import itertools
n = int(input())
max_step = n // 2
min_diff = math.inf

visited = [False] * n

matrix = [
    list(map(int, input().split())) 
        for _ in range(n)
]
sum_matrix = [
    [0] * n for _ in range(n)
]

for i in range(n):
    for j in range(n):
        if i == j: continue
        sum_matrix[i][j] += matrix[i][j]
        sum_matrix[j][i] += matrix[i][j]

nCr = list(itertools.combinations([i for i in range(n)], n // 2))

team_a_list = nCr[:len(nCr)//2]
team_b_list = list(reversed(nCr[len(nCr)//2:]))

for i in range(len(nCr) // 2):
    total_a = total_b = 0
    comb_a = list(itertools.combinations(team_a_list[i], 2))
    comb_b = list(itertools.combinations(team_b_list[i], 2))
    for x, y in comb_a:
        total_a += sum_matrix[x][y]
    for x, y in comb_b:
        total_b += sum_matrix[x][y]
    min_diff = min(min_diff, abs(total_a - total_b))

print(min_diff)