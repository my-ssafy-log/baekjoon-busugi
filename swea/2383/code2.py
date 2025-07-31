T = int(input())

for t in range(T):
    N = int(input())

    ppos_list = []
    spos_list = [] # [(계단1 x좌표, 계단1 y좌표), (계단2 x좌표, 계단2 y좌표)]

    for i in range(N):
        row = list(map(int, input().split()))
        
        for j, cell in enumerate(row):
            if cell == 1:
                ppos_list.append((i, j))
            if cell >= 2:
                spos_list.append((i, j))
    # 입력된 리스트 튜플로 고정
    ppos_list = tuple(ppos_list) 
    spos_list = tuple(spos_list)

    done = [False] * len(ppos_list)

    def compare(ppos_sidx):
        ppos, sidx = ppos_sidx
        s = spos_list[sidx]
        return abs(ppos[0] - s[0]) + abs(ppos[1] - s[1])

    def brute_force(ppos_sidx_list):
        step = len(ppos_sidx_list)

        if len(ppos_list) == step:
            sorted(ppos_sidx_list, key=compare)
            return

        brute_force(ppos_sidx_list + [(ppos_list[step], 0)])
        brute_force(ppos_sidx_list + [(ppos_list[step], 1)])

    brute_force([(ppos_list[0], 0)])
    brute_force([(ppos_list[0], 1)])