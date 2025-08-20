#
# N x N (7 <= N <= 12)
# 1은 코어
#
#
#
#
#
#
#
from collections import defaultdict
from pprint import pprint
 
T = int(input())
 
for t in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
 
    pos_list = []
    processor_dirs = defaultdict(list)
 
    rows = [False] * (N + 1)
    columns = [False] * (N + 1)
    # 왼쪽, 상단으로 전선 깔 수 있는 프로세서 찾고
    # 왼쪽, 상단 갈 수 있다고 방향 값 추가하기
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                pos_list.append((i, j))
                if not rows[i]:
                    rows[i] = True
                    processor_dirs[(i, j)].append((0, -1))
                if not columns[j]:
                    columns[j] = True
                    processor_dirs[(i, j)].append((-1, 0))
 
    rows = [False] * (N + 1)
    columns = [False] * (N + 1)
 
    # 오른쪽, 하단으로 전선 깔 수 있는 프로세서 찾고
    # 방향 값 추가하기
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if board[i][j] == 1:
                if not rows[i]:
                    rows[i] = True
                    processor_dirs[(i, j)].append((0, 1))
                if not columns[j]:
                    columns[j] = True
                    processor_dirs[(i, j)].append((1, 0))
    pos_list.sort(key=lambda pos: len(processor_dirs[pos]))
 
    def get_len(pos, d):
        x, y = pos
        if d == (-1, 0):
            return x
        elif d == (1, 0):
            return N - x - 1
        elif d == (0, -1):
            return y
        else:
            return N - y - 1
 
    min_l = 10**18
    total_l = 0
    max_processors = -1
 
    connections = {}
 
    def can_connect(pos, d):
        x, y = pos
        for pos2, d2 in connections.items():
            x2, y2 = pos2
            if d == (-1, 0) and x2 < x:
                if y2 < y and d2 == (0, 1) or y2 > y and d2 == (0, -1):
                    return False
            elif d == (1, 0) and x2 > x:
                if y2 < y and d2 == (0, 1) or y2 > y and d2 == (0, -1):
                    return False
            elif d == (0, -1) and y2 < y:
                if x2 > x and d2 == (-1, 0) or x2 < x and d2 == (1, 0):
                    return False
            elif d == (0, 1) and y2 > y:
                if x2 > x and d2 == (-1, 0) or x2 < x and d2 == (1, 0):
                    return False
        return True
 
    def dfs(step, processor_cnt=0):
        global max_processors, min_l, total_l, copy_connections
        if step == len(pos_list):
            if processor_cnt > max_processors:
                # print(connections)
                max_processors = processor_cnt
                min_l = total_l
            elif processor_cnt == max_processors:
                min_l = min(min_l, total_l)
            return
 
        pos = pos_list[step]
 
        for d in processor_dirs[pos]:
            if not can_connect(pos, d):
                continue
            connections[pos] = d
            l = get_len(pos, d)
            total_l += l
 
            dfs(step + 1, processor_cnt+1)
            total_l -= l
            del connections[pos]
        if len(pos_list) - max_processors + processor_cnt > step:
            dfs(step + 1, processor_cnt)
 
    dfs(0)
    # print(pos_list)
    print(f"#{t+1}", min_l)