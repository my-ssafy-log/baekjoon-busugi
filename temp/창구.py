import sys

sys.stdin = open('sample_input.txt', 'r')

from collections import deque
#
#
T = int(input())

for t in range(T):
    N, M, K, A, B = map(int, input().split())

    A_LIST = [0] + list(map(int, input().split()))
    B_LIST = [0] + list(map(int, input().split()))
    t_list = [(i+1, arrv) for i, arrv in enumerate(input().split())]
    t_list.sort(key=lambda ele: (ele[1], ele[0]))

    a_counter = [None] * (A+1)  # None | (고객번호표, 창구에서의 시간)
    b_counter = [None] * (B+1)  # None | (고객번호표, 창구에서의 시간)
    a_waiting = deque()
    b_waiting = deque()

    # 오픈런 한 사람 (0에 도착한 사람) A 창구 웨이팅에 넣기
    i = 1
    for custno, arrv in t_list:
        if arrv == 0:
            a_waiting.append(custno)
        else:
            break

    while a_waiting or b_waiting:
        # 비어있는 A 창구에 A 웨이팅에 있는 사람 넣기
        for i, counter in enumerate(a_counter[1:], 1):
            if counter is None:
                custno = a_waiting.popleft()
                a_counter[i] = (custno, 1)
