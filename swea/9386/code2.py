T = int(input())

for t in range(T):
    N = int(input())
    nums = list(map(int, list(input())))
    a = [0] * N

    max_v = 0

    for i in range(1, N):
        nums[i] = nums[i] * (nums[i] + nums[i-1])
        max_v = max(max_v, nums[i])
    print(f"#{t+1} {max_v}")