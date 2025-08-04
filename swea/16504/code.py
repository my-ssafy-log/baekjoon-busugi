T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    res = []
    for i in range(0, len(arr)):
        cnt = 0
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                cnt += 1
        res.append(cnt)
    print(f"#{t+1} {max(res)}")