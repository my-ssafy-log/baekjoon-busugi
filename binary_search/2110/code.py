import sys
import math
from bisect import bisect_left

def readline():
    return sys.stdin.readline().rstrip()

N, C = map(int, readline().split())

arr = []

for i in range(N):
    arr.append(int(readline()))
arr.sort() # 집 위치를 오름차순으로 정렬, 수평 좌표로 봤을 때 가장 왼쪽에 있는 집을 시작으로 가장 오른쪽에 있는 집 좌표를 끝으로 나열되게 정렬

if C == 2:
    print(arr[-1] - arr[0])
    exit()

min_diff = math.inf # 집들 사이 거리 중 가장 짧은 거리
for i in range(len(arr) - 1):
    min_diff = min(min_diff, arr[i+1] - arr[i])

# 0번째 집부터 거리가 dist 이상만큼 떨어진 집들 중 
# 가장 왼쪽에 위치한 집에 공유기를 설치한다고 했을 때
# 공유기가 C개 설치가 되었는가? 를 True, False로 반환함
def is_installed_C_router(arr, dist):
    cnt = 1

    # 공유기를 선택하는 가장 왼쪽에 있는 집의 index 위치
    left_house_idx = 0
    i = 1
    while left_house_idx < len(arr) and i < len(arr):
        if arr[i] - arr[left_house_idx] >= dist:
            left_house_idx = i
            cnt += 1
        else:
            i += 1
        if cnt >= C:
            break
    
    # 공유기 C개 설치했는가?
    return cnt >= C

# 공유기 C개를 설치했을 때 가까운 거리 중 가장 큰 가까운 거리
max_min_dist = -1

s = min_diff # 집 사이 거리 중 제일 짧은 거리
# 양 끝단에 있는 집 사이 거리를 C-1 로 나눴을 때 나오는 거리
# max_min_dist의 값이 양 끝단에 있는 집 사이 거리를 C-1로 나눴을 때의 거리값보다 커질 수 없기 때문에
# 이 값을 e로 설정함
e = (arr[-1] - arr[0]) // (C-1)

while s <= e:
    mid = (s + e) // 2
    # 가장 인접한 집 사이의 거리의 최대 거리를 mid 값이라고 가정했을 때 공유기가 C개 충분히 다 설치 됐는지 True, False로 받음
    is_installed_enough = is_installed_C_router(arr, mid)

    # 만약 C개 설치가 됐다면?
    if is_installed_enough:
        # 공유기를 C개 설치할 때 가정한 거리값들 중 가장 큰 값을 max_min_dist에 넣음
        max_min_dist = max(max_min_dist, mid)
        s = mid + 1
    else: # C개 설치가 안됐다면? 가장 인접한 집 사이 거리가 크다는 말이므로, 크기를 줄임
        e = mid - 1
print(max_min_dist)
