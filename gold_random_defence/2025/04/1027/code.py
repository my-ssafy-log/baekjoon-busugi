import sys
sys.stdin = open('gold_random_defence/2025/04/1027/sample_input.txt')

N = int(input())

arr = list(map(int, input().split()))

max_cnt = 0
for i in range(N):
    cnt = 0

    # 왼쪽 탐색
    min_left_slope = float('inf')
    for left in range(i-1, -1, -1):
        slope = (arr[i] - arr[left]) / (i - left)
        if slope < min_left_slope:
            min_left_slope = slope
            cnt += 1
    
    max_right_slope = float('-inf')
    for right in range(i+1, N, 1):
        slope = (arr[right] - arr[i]) / (right - i)
        if slope > max_right_slope:
            max_right_slope = slope
            cnt += 1

    max_cnt = max(max_cnt, cnt)

print(max_cnt)
