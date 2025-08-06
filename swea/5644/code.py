import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for t in range(T):
    M, A = map(int, input().split())

    A_DIRECTIONS = list(map(int, input().split()))
    B_DIRECTIONS = list(map(int, input().split()))

    a_power_list = []
    b_power_list = []

    bc_dict = {}
    bc_list = []
    for i in range(A):
        y, x, c, p = map(int, input().split())
        bc_list.append({'pos': (x, y), 'c': c, 'p': p})
        bc_dict[(x, y)] = {'c': c, 'p': p}
    # c를 기준으로 내림차순 정렬
    bc_list.sort(key=lambda bc: -bc['p'])

    a_pos = (1, 1)
    b_pos = (10, 10)

    def get_able_bcs(pos):
        x, y = pos

        possible_bcs = []
        for bc in bc_list:
            bcx, bcy = bc['pos']

            if abs(bcx - x) + abs(bcy - y) <= bc['c']:
                possible_bcs.append((bcx, bcy))
            # 겹칠 것을 고려해 2개 이상이면 break
            if len(possible_bcs) >= 2:
                break
        return possible_bcs

    def add_power():
        a_able_bcs = get_able_bcs(a_pos)
        a_bcs_len = len(a_able_bcs)
        b_able_bcs = get_able_bcs(b_pos)
        b_bcs_len = len(b_able_bcs)

        a_able_bc = a_able_bcs[0] if a_able_bcs else (-1, -1)
        b_able_bc = b_able_bcs[0] if b_able_bcs else (-2, -2)

        if a_able_bc == b_able_bc:
            if a_bcs_len == b_bcs_len == 2:
                if a_able_bcs[1] > b_able_bcs[1]:
                    a_able_bc = a_able_bcs[1]
                else:
                    b_able_bc = b_able_bcs[1]
            elif a_bcs_len == 2:
                a_able_bc = a_able_bcs[1]
            elif b_bcs_len == 2:
                b_able_bc = b_able_bcs[1]

        if a_able_bc == b_able_bc:
            bc = bc_dict[a_able_bc]
            a_power = b_power = bc['p'] // 2
        else:
            a_bc = bc_dict.get(a_able_bc, {'p': 0})
            b_bc = bc_dict.get(b_able_bc, {'p': 0})
            a_power, b_power = a_bc['p'], b_bc['p']
        a_power_list.append(a_power)
        b_power_list.append(b_power)

    def get_next_pos(pos, d):
        dx = [0, -1, 0, 1, 0]
        dy = [0, 0, 1, 0, -1]
        return pos[0] + dx[d], pos[1] + dy[d]

    add_power()
    for i in range(M):
        a_pos = get_next_pos(a_pos, A_DIRECTIONS[i])
        b_pos = get_next_pos(b_pos, B_DIRECTIONS[i])
        add_power()
    print(f"#{t+1} {sum(a_power_list) + sum(b_power_list)}")
