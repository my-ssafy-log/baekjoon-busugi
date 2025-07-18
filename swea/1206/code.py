for t in range(10):
    n = int(input())
    arr = list(map(int, input().split()))
    total = 0
    for i in range(n):
        max_v = 0
        if i == 0:
            max_v = max(arr[1:3])
        elif i == 1:
            max_v = max(arr[0], arr[2], arr[3])
        elif i == n - 2:
            max_v = max(arr[n-1], arr[n-3], arr[n-4])
        elif i == n - 1:
            max_v = max(arr[n-3:n-1])
        else:
            max_v = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
        total += max(arr[i] - max_v, 0)
    print(f"#{t+1} {total}")