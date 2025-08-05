from itertools import combinations
from pprint import pprint

T = int(input())


def test(film, K):
    film_T = list(zip(*film))
    # pprint(film_T)
    for column in film_T:
        prev = None
        cnt = 0
        for cell in column:
            if prev is None:
                prev = cell
                cnt += 1
            elif prev == cell:
                cnt += 1
            else:
                prev = cell
                cnt = 1

            if cnt == K:
                break
        if cnt < K:
            return False
    return True


for t in range(T):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    origin_film = film[:]

    is_ok = test(film, K)
    if is_ok:
        print(f"#{t + 1} 0")
        continue

    # 선택할 행을 리스트로 담음
    PICK_LIST = list(range(D))
    DRUGS = [
        [0] * W,
        [1] * W
    ]

    def f(ci, step, d):
        global film, is_ok
        if step == d:
            return test(film, K)

        for j in range(ci, D):
            film[j] = DRUGS[0]
            is_ok = f(j + 1, step + 1, d)
            if is_ok:
                return is_ok
            film[j] = origin_film[j]
            film[j] = DRUGS[1]
            is_ok = f(j + 1, step + 1, d)
            if is_ok:
                return is_ok
            film[j] = origin_film[j]
        pass

    # d개의 막에 약물을 투입함. 1...K
    max_d = 0
    for d in range(1, K + 1):
        if is_ok:
            break
        for i in range(0, D):
            film[i] = DRUGS[0]
            is_ok = f(i+1, 1, d)
            if is_ok:
                max_d = d
                break
            film[i] = origin_film[i]
            film[i] = DRUGS[1]
            is_ok = f(i+1, 1, d)
            if is_ok:
                max_d = d
                break
            film[i] = origin_film[i]
    print(f"#{t+1} {max_d}")
