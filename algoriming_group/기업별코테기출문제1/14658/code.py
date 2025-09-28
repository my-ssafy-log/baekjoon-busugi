N, M, L, K = map(int, input().split())

sstars = []
vertex_xs = []
vertex_ys = []
for _ in range(K):
    x, y = map(int, input().split())
    sstars.append((x, y))
    vertex_xs.append(x)
    vertex_ys.append(y)

def is_include(sstar, x_range, y_range):
    return (x_range[0] <= sstar[0] <= x_range[1] and 
            y_range[0] <= sstar[1] <= y_range[1])

max_cnt = 0
# L x L 트램펄린을 sstar를 트램펄린 구석에 두는 위치로 뒀을 때
# 구석을 기준으로 4분면을 확인해 포함하는 별의 개수
for vertex_x in vertex_xs:
    for vertex_y in vertex_ys:
        # print('vertex:', vertex_x, vertex_y)
        for dx, dy in [(-1, 1), (-1, -1), (1, -1), (1, 1)]:
            x_range = vertex_x, vertex_x + L * dx
            y_range = vertex_y, vertex_y + L * dy
            
            sx, ex = min(x_range), max(x_range)
            sy, ey = min(y_range), max(y_range)
            # print(f'sx: {sx}, sy: {sy}')
            # print(f'ex: {ex}, ey: {ey}')
        
            cnt = 0
            for sstar in sstars:
                if is_include(sstar, (sx, ex), (sy, ey)):
                    cnt += 1
            # print(cnt)
            max_cnt = max(max_cnt, cnt)
        # print('=' * 30)
print(K - max_cnt)

"""
12 10 4 7
2 4
7 3
3 1
5 6
4 7
12 10
8 6

x x x x x x x x x x x
x x x x x x x x x x x
x x x x o x x x x x x
x o x x x x x x x x x
x x x x x x x o x x x
x x x x x x o x x x x
x x x x x x x x x x x
x x x o x x x x x x x
x x x x x x o x x x x
x x x x x x x x x x x
x x x x x x x x x x x
x x x x x x x x x x x
x x x x x x x x x x o


"""

