sudoku = [list(map(int, input().split())) for _ in range(9)]

arr = []

## (행/열/사각형 번호, 숫자)로 숫자가 존재하는지 유무를 저장하는 변수
# (행, 숫자)
rows_map = [[False] * 10 for _ in range(9)]
# (열, 숫자)
cols_map = [[False] * 10 for _ in range(9)]
# (사각형 번호, 숫자)
sqrs_map = [[False] * 10 for _ in range(9)]

def get_square_number(i, j):
    return (i // 3) * 3 + j // 3

for i in range(9):
    for j in range(9):
        cell = sudoku[i][j]
        if cell == 0:
            arr.append((i, j))
        else:
            rows_map[i][cell] = True
            cols_map[j][cell] = True
            sqrs_map[get_square_number(i, j)][cell] = True

# print("Row")
# for row in rows_map:
#     print(row)
# print("\nColumns")
# for column in columns_map:
#     print(column)
# print("\nSquares")
# for squares in squares_map:
#     print(squares)

def f(step):
    if len(arr) == step:
        # print('test')
        for row in sudoku:
            print(' '.join(map(str, row)))
        quit()

    # for x, y in arr:
    i, j = arr[step]
    for num in range(1, 10):
        if rows_map[i][num]: continue
        if cols_map[j][num]: continue
        if sqrs_map[get_square_number(i, j)][num]: continue

        rows_map[i][num] = True
        cols_map[j][num] = True
        sqrs_map[get_square_number(i, j)][num] = True
        sudoku[i][j] = num
        # print(f"({i}, {j}): {num}")
        f(step + 1)
        rows_map[i][num] = False
        cols_map[j][num] = False
        sqrs_map[get_square_number(i, j)][num] = False
        sudoku[i][j] = 0


i, j = arr[0]
for num in range(1, 10):
    if  rows_map[i][num] or \
        cols_map[j][num] or \
        sqrs_map[get_square_number(i, j)][num]: continue
    
    rows_map[i][num] = True
    cols_map[j][num] = True
    sqrs_map[get_square_number(i, j)][num] = True
    sudoku[i][j] = num

    # print(f"({i}, {j}): {num}")
    f(1)

    rows_map[i][num] = False
    cols_map[j][num] = False
    sqrs_map[get_square_number(i, j)][num] = False
    sudoku[i][j] = 0