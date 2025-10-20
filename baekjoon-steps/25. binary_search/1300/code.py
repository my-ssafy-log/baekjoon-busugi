N = int(input())
K = int(input())


def get_lte_num(cmp):
    num = 0
    for i in range(1, N+1):
        num += min(cmp // i, N)
    return num

start = 1
end = N ** 2 + 1
min_num = float('inf')
while start < end:
    # print(start, end)
    mid = (start + end) // 2
    lte_num = get_lte_num(mid)
    if lte_num >= K:
        end = mid
        min_num = min(min_num, end)
    elif lte_num < K:
        start = mid + 1
    # else:
    #     min_num = min(min_num, end)

print(min_num)
