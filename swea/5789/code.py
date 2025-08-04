T = int(input())

for t in range(T):
    N, Q = map(int, input().split())
    arr = [0] * (N+1)
    for q in range(Q):
        L, R = map(int, input().split())
        for i in range(L, R+1):
            arr[i] = q+1
    print(f"#{t+1} {' '.join(map(str, arr[1:]))}")
