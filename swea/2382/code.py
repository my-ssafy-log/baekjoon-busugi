# import sys

def readline():
    return input()

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
reversed_d = [0, 2, 1, 4, 3]

T = int(readline())

# 상: 1
# 하: 2
# 좌: 3
# 우: 4
for t in range(T):
    N, M, K = map(int, readline().split())
    
    mic_list = []
    total = 0
    for k in range(K):
        x, y, num, d = map(int, readline().split())
        mic_list.append({
            'pos': (x, y),
            'num': num,
            'd': d
        })
        total += num

    def move_mic(pos, num, d):
        global total
        nx = pos[0] + dx[d]
        ny = pos[1] + dy[d]

        if nx == 0 or nx == N-1 or ny == 0 or ny == N-1:
            d = reversed_d[d]
            total -= num - num//2
            num //= 2
        return ((nx, ny), num, d)
    
    def do_next():
        global mic_list
        new_mic_list = []
        new_mic_dict: dict[tuple[int, int], list[dict[str, int]]] = {}
        for mic in mic_list:
            pos, num, d = move_mic(**mic)
            new_mic_dict.setdefault(pos, [])
            new_mic_dict[pos].append({
                'num': num,
                'd': d
            })

        # print(new_mic_dict)
        for new_mic_pos in new_mic_dict:
            total_num = 0
            max_d = 0
            max_num = 0
            for new_mic in new_mic_dict[new_mic_pos]:
                total_num += new_mic['num']
                if max_num < new_mic['num']:
                    max_num = new_mic['num']
                    max_d = new_mic['d']
            new_mic_list.append({
                'pos': new_mic_pos,
                'num': total_num,
                'd': max_d
            })

        mic_list = new_mic_list

    for m in range(M):
        do_next()
    print(f"#{t+1} {total}")