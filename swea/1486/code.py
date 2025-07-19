t = int(input())

for test_case in range(t):
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = 1
    for v in arr:
        dp |= dp << v
    min_v = None
    
    for i in range(b, dp.bit_length()):
        if dp >> i & 1:
            min_v = i
            break
    print(f"#{test_case + 1} {min_v - b}")