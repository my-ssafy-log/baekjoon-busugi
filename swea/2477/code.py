from collections import deque
import heapq

T = int(input())

for t in range(T):
    N, M, K, A, B = map(int, input().split())
    at_arr = [0] + list(map(int, input().split()))
    a_arr = [(0, 0)] * (N+1) # (고객번호, 보낸 시간)
    bt_arr = [0] + list(map(int, input().split()))
    b_arr = [(0, 0)] * (M+1) # (고객번호, 보낸 시간)

    t_arr = list(map(int, input().split()))
    t_arr = [(i+1, t) for i, t in enumerate(t_arr)] # (고객번호, 시간)
    # 도착하는 시간대로 정렬
    t_arr.sort(key=lambda t: (t[1], t[0]))
    # [고객번호]: 방문창고번호
    visited = [{'a': 0, 'b': 0} for _ in range(K+1)]
    # 고객의 정비 받고 상태
    is_visiting = [False] * (K+1)

    cnt = 0

    # 고객번호
    a_waiting_queue = []
    b_waiting_queue = []

    time = 0
    total = 0

    last_customer_number = t_arr[-1][0]

    # 마지막으로 도착하는 고객 번호가 b창구에 아직 방문하지 않았다면
    while cnt < K:
        # 정비소에 도착한 사람들을 a 창고 대기열에 추가함
        while len(t_arr) > 0 and t_arr[0][1] == time:
            cnum = t_arr[0][0]
            t_arr = t_arr[1:]
            a_waiting_queue.append(cnum)

        # a 창고에 있는 사람들의 보낸 시간을 +1 해줌
        for i in range(1, N+1):
            # 비어있지 않다면
            if a_arr[i][0] != 0:
                a_arr[i] = (a_arr[i][0], a_arr[i][1]+1)

        ##### 내보내고 #####
        # a 창고에 있는 사람들이 보낸 시간이 창고의 시간과 같아진다면 (안전하게 같거나 커진다면)
        for i in range(1, N+1):
            if a_arr[i][1] == at_arr[i]:
                # visited에 기록함
                visited[a_arr[i][0]]['a'] = i
                # b 창고 대기열에 추가함
                b_waiting_queue.append(a_arr[i][0])
                a_arr[i] = (0, 0)

        ##### 추가하기 #####
        # 비어있는 a 창고에 대기열에 있는 사람을 한명씩 가져옴
        for i in range(1, N+1):
            if a_arr[i][0] == 0:
                if len(a_waiting_queue) == 0:
                    break
                cnum = a_waiting_queue[0]
                a_waiting_queue = a_waiting_queue[1:]
                a_arr[i] = (cnum, 0)
        
        # a_waiting_queue.sort()

        # b 창고에 있는 사람들의 보낸 시간을 +1 해줌
        for i in range(1, M+1):
            # 비어있지 않다면
            if b_arr[i][0] != 0:
                b_arr[i] = (b_arr[i][0], b_arr[i][1]+1)
        
        ##### 내보내고 #####
        # b 창고에 있는 사람들이 보낸 시간이 창고의 시간과 같아진다면
        for i in range(1, M+1):
            if b_arr[i][1] == bt_arr[i]:
                # visited에 기록함
                visited[b_arr[i][0]]['b'] = i
                # 만약 방문 기록이 A, B와 같다면
                if (visited[b_arr[i][0]]['a'] == A and
                    visited[b_arr[i][0]]['b'] == B):
                    total += b_arr[i][0]
                # 내보냄
                b_arr[i] = (0, 0)
                cnt += 1

        ##### 추가하기 #####
        # 비어있는 b 창고에 대기열에 있는 사람을 한명식 가져옴
        for i in range(1, M+1):
            if b_arr[i][0] == 0:
                if len(b_waiting_queue) == 0:
                    break
                cnum = b_waiting_queue[0]
                b_waiting_queue = b_waiting_queue[1:]
                b_arr[i] = (cnum, 0)
        # b_waiting_queue.sort()

        # print("time:", time)
        # print("a_arr:", a_arr)
        # print("b_arr:", b_arr)
        # print("visited", visited)
        # print()
        time += 1

        # breakpoint()
    # print("visited")
    # print(visited)
    if total == 0:
        print(f"#{t+1} -1")
    else:
        print(f"#{t+1} {total}")