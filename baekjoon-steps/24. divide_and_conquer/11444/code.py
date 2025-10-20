import sys

DIVISOR = 1_000_000_007
BASE_MATRIX = [
    [1, 1],
    [1, 0]
]

def readline():
    return sys.stdin.readline().rstrip()

N = int(readline())

def multiply_2x2_matrix(A, B):
    matrix = [
        [0, 0],
        [0, 0]
    ]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                matrix[i][j] += ((A[i][k] % DIVISOR) * (B[k][j] % DIVISOR) % DIVISOR)
    return matrix

memo = {
    1: BASE_MATRIX
}

def f(n):
    if n in memo:
        return memo[n]
    if n % 2 == 1:
        memo[n] = multiply_2x2_matrix(
            BASE_MATRIX,
            multiply_2x2_matrix(
                f(n // 2),
                f(n // 2)
            )
        )
    else:
        memo[n] = multiply_2x2_matrix(
            f(n // 2),
            f(n // 2)
        )
    return memo[n]

print(f(N+1)[1][1] % DIVISOR)
