import sys
import math

def readline():
    return sys.stdin.readline().rstrip()

N, C = map(int, readline().split())

arr = []

for i in range(N):
    arr.append(int(readline()))
arr.sort() # 집 위치를 오름차순으로 정렬, 수평 좌표로 봤을 때 가장 왼쪽에 있는 집을 시작으로 가장 오른쪽에 있는 집 좌표를 끝으로 나열되게 정렬

min_diff = math.inf # 집들 사이 거리 중 가장 짧은 거리
for i in range(len(arr) - 1):
    min_diff = min(min_diff, arr[i+1] - arr[i])

# arr에서 num보다 크거나 같은 값의 index를 찾음
# 만약 num보다 크거나 같은 값이 없다면 len(arr)의 값을 반환함
def binary_search(arr, num):
    s = 0
    e = len(arr) - 1
    min_max_idx = len(arr)
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] < num:
            s = mid + 1
        else:
            min_max_idx = mid
            e = mid - 1
    return min_max_idx

# 0번째 집부터 거리가 dist 이상만큼 떨어진 집들 중 
# 가장 왼쪽에 위치한 집에 공유기를 설치한다고 했을 때
# 공유기가 C개 설치가 되었는가? 를 True, False로 반환함
def is_installed_C_router(arr, dist):
    cnt = 1

    # 공유기를 선택하는 가장 왼쪽에 있는 집의 index 위치
    left_house_idx = 0
    while left_house_idx < len(arr) - 1:
        # 가장 왼쪽에 있는 집 다음 집들 중에서 거리값 이상으로 떨어진 집들 중 가장 가까운 집과
        # 몇 칸 멀어져 있는지를 반환함
        # 아래 이중 탐색으로 공유기를 설치할 위치를 탐색하는 것
        idx = binary_search(arr[left_house_idx+1:], arr[left_house_idx] + dist)

        # 가장 왼쪽에 있는 집과, 거리 이상으로 떨어진 집들 중 가까운 집과 멀어진 칸 수를
        # left_house_idx에 넣음 따라서 left_house_idx의 의미는
        # 가장 왼쪽에 있는 집과 거리 이상으로 떨어진 가까운 집의 index가 됨
        left_house_idx += idx+1

        # 만약 left_house_idx의 값이 len(arr)과 같다면, 거리 이상으로 떨어진 집들이 하나도 없다는 의미이므로
        # break를 함
        if left_house_idx == len(arr):
            break

        # 공유기 하나를 설치했으므로 1을 더함
        cnt += 1
        # 공유기 C개 설치 완료했으면 break
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
    # 최소 집과 집 사이 떨어진 거리를 mid 값으로 잡았을 때 공유기가 C개 설치 됐는지 True, False로 받음
    is_installed_enough = is_installed_C_router(arr, mid)

    # 만약 C개 설치가 됐다면?
    if is_installed_enough:
        # 공유기를 C개 설치할 때 가까운 거리 중 가장 큰 가까운 거리값을 max로 갱신함
        max_min_dist = max(max_min_dist, mid)
        s = mid + 1
    else:
        e = mid - 1
print(max_min_dist)
