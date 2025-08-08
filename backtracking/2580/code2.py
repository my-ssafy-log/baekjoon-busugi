import sys
sys.stdin = open('sample_input.txt', 'r')

from pprint import pprint

sudoku = []

rows = [0] * 9
cols = [0] * 9
sqrs = [0] * 9

empty_pos = []


def set_num(i, j, num):
    rows[i] |= 1 << num
    cols[j] |= 1 << num
    sqrs[i // 3 * 3 + j // 3] |= 1 << num


def unset_num(i, j, num):
    rows[i] &= ~(1 << num)
    cols[j] &= ~(1 << num)
    sqrs[i // 3 * 3 + j // 3] &= ~(1 << num)


for i in range(9):
    row = list(map(int, input().split()))
    for j, num in enumerate(row):
        if num == 0:
            empty_pos.append((i, j))
            continue

        set_num(i, j, num)
    sudoku.append(row)


def fill(step):
    if step == len(empty_pos):
        for row in sudoku:
            print(*row)
        exit()
    
    for num in range(1, 10):
        i, j = empty_pos[step]
        if ((rows[i] >> num) & 1 == 1 or 
            (cols[j] >> num) & 1 == 1 or 
            (sqrs[i // 3 * 3 + j // 3] >> num) & 1 == 1):
            continue

        set_num(i, j, num)
        sudoku[i][j] = num
        fill(step + 1)
        unset_num(i, j, num)

fill(0)
