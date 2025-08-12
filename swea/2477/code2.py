import sys
sys.stdin = open('sample_input.txt', 'r')

from collections import deque
#
#
T = int(input())

for t in range(T):
    N, M, K, A, B = map(int, input().split())

    A_TIMES = [0] + list(map(int, input().split()))
    B_TIMES = [0] + list(map(int, input().split()))
    t_list = [(i+1, arrv) for i, arrv in enumerate(list(map(int, input().split())))]
    t_list.sort(key=lambda ele: (ele[1], ele[0]))
    t_q = deque(t_list)

    a_waiting = deque()
    b_waiting = deque()
    a_counter = [None] * (N+1)  # None | (고객번호표, 창구에서의 시간)
    b_counter = [None] * (M+1)  # None | (고객번호표, 창구에서의 시간)

    done = 0
    hist = {custno: [] for custno in range(1, K + 1)}

    elapsed_time = 0
    while done < K:
        # A 창구 웨이팅에 추가하기
        while t_q and t_q[0][1] == elapsed_time:
            a_waiting.append(t_q.popleft()[0])

        # A 창구 시간 다 보냈는지 확인하기
        for i in range(1, N+1):
            if a_counter[i] is None:
                continue
            if a_counter[i][1] == A_TIMES[i]:
                b_waiting.append(a_counter[i][0])
                a_counter[i] = None

        # A 창구 웨이팅에서 빈 A 창구 넣어주기
        for i in range(1, N+1):
            if a_counter[i] is not None:
                continue
            if not a_waiting:
                break
            custno = a_waiting.popleft()
            hist[custno].append(i)
            a_counter[i] = (custno, 0)

        # A 창구 시간 보내기
        for i in range(1, N+1):
            if a_counter[i] is None:
                continue
            custno, tm = a_counter[i]
            a_counter[i] = (custno, tm + 1)
        
        # B 창구 시간 다 보냈는지 확인하기
        for i in range(1, M+1):
            if b_counter[i] is None:
                continue
            if b_counter[i][1] == B_TIMES[i]:
                b_counter[i] = None
        
        # B 창구 웨이팅에서 빈 B 창구 넣어주기
        for i in range(1, M+1):
            if b_counter[i] is not None:
                continue
            if not b_waiting:
                break
            custno = b_waiting.popleft()
            hist[custno].append(i)
            done += 1
            b_counter[i] = (custno, 0)
        
        # B 창구 시간 보내기
        for i in range(1, M+1):
            if b_counter[i] is None:
                continue
            custno, tm = b_counter[i]
            b_counter[i] = (custno, tm + 1)
        elapsed_time += 1

    total = 0
    for key, value in hist.items():
        if value[0] == A and value[1] == B:
            total += key
    print(f"#{t+1}", total if total else -1)