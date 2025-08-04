T = int(input())


def test(film, K):
    for i in range(len(film[0])):
        prev = None
        cnt = 0
        for j in range(len(film)):
            if prev == None:
                prev = film[j][i]
                cnt += 1
            elif prev == film[j][i]:
                cnt += 1
            else:
                prev = film[j][i]
                cnt = 1
            if cnt == K:
                break
        if cnt < K:
            return False
    return True

for t in range(T):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    origin_film = film[:] # film의 i번 막에 약물을 투입하고 다시 복원을 하기 위해 복사를 함

    if K == 1:
        print(f"#{t + 1} 0")
        continue

    # 약물을 0개 투입했을 때 test를 수행함
    # is_ok는 test가 완료됐는지 안됐는지를 담는 변수, 아래에서 for문에서 수행하는 테스트에서도 쓰임
    is_ok = test(film, K)
    if is_ok:
        print(f"#{t + 1} 0")
        continue

    # 필름에 넣을 약물을 담음 film[1] = DRUGS[0]이면 1번 막에 약물 0을 투입한다는 의미
    DRUGS = [
        [0] * W,
        [1] * W
    ]

    def dfs(ci, step, d):
        global film, is_ok
        if d == K:
            return True

        if step == d: # 막약 현재 투입된 약물 수와 투입되야 할 약물 수가 같다면
            return test(film, K) # test 한 후 결과 값을 반환함

        # 75번째 코드와 똑같이 동작함
        for i in range(ci, D):
            film[i] = DRUGS[0] # i번에 약물 9을 투입
            is_ok = dfs(i + 1, step + 1, d) # dfs 돌리고
            if is_ok: # test 결과가 True라면
                return is_ok # is_ok 반환
            film[i] = DRUGS[1]
            is_ok = dfs(i + 1, step + 1, d)
            if is_ok:
                return is_ok
            film[i] = origin_film[i]
        pass

    ans = 0
    # d개의 막에 약물을 투입함. 그런데 1개만 투입하는 것부터 K개까지 투입하는 것까지 순서대로 투입함
    for d in range(1, K + 1):
        is_ok = dfs(0, 0, d)
        if is_ok:
            ans = d
            break
        # 0번 막부터 D-1번 막까지 몇번재에 약물이 처음 들어가는지 나타냄

    print(f"#{t+1} {ans}")
