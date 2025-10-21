memo = [[[0] * 101 for _ in range(101)] for _ in range(101)]
is_calculated = [[[False] * 101 for _ in range(101)] for _ in range(101)]

def w(a, b, c):
    if is_calculated[a][b][c]:
        return memo[a][b][c]
    
    if a <= 0 or b <= 0 or c <= 0:
        is_calculated[a][b][c] = True
        memo[a][b][c] = 1
        return 1
    
    if a > 20 or b > 20 or c > 20:
        is_calculated[a][b][c] = True
        memo[a][b][c] = w(20, 20, 20)
        return memo[a][b][c]
    
    if a < b and b < c:
        is_calculated[a][b][c] = True
        memo[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memo[a][b][c]

    is_calculated[a][b][c] = True
    memo[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return memo[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")