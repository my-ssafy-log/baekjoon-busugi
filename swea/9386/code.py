T = int(input())

for t in range(T):
    N = int(input())
    str = input()
    a = [0] * (N)
    max_v = 0

    for i in range(0, N):
        if str[i] == '1':
            if i == 0:
                a[i] = 1
            else:
                a[i] = a[i-1] + 1
            max_v = max(a[i], max_v)
    print(f"#{t+1} {max_v}")