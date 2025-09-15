# 2110 공유기 설치

[링크](https://www.acmicpc.net/problem/2110)

## 문제 해설
이 문제는 수평선 위에 N개의 집의 좌표가 주어지고 N개의 집들 중 C개에 공유기를 설치한다고 할 때  
임의의 C개의 집에 공유기를 설치했을 때  
설치한 공유기 사이 거리들 중 가장 가까운 거리의 최댓값을 구하는 문제이다.  
집의 위치값을 $x$라고 할 때 N, C, x의 범위는  
 $2 \leq N \leq 200,000$,  
 $2 \leq C \leq N$,  
 $0 \leq x_i \leq 1,000,000,000$
이다.

이 문제는 결과값을 최소화 또는 최대화 해야하는 '최적화 문제'를  
이 결과값을 임의로 지정해서 이 값이 만족하는지 '예' 또는 '아니오'로 답하는 '결정 문제'로 바꾸어 푸는 문제이다.  

예를 들어 정수 X 중에 10보다 작은 최댓값을 찾으라는 문제가 있고, X의 범위가 1 ~ 15 이라면,  
이분 탐색을 이용하여  
`max_v = -1`
1. $\lfloor(1_s + 15_e) / 2\rfloor = 8$, 5는 10보다 작은가? O
    `max_v` 보다 8이 크므로 `max_v`를 8로 갱신, $s$는 8+1인 9로 갱신
2. $\lfloor(9_s + 15_e) / 2\rfloor = 12$, 12은 10보다 작은가? X
    `max_v`는 건드리지 않고, $e$를 12-1인 11로 갱신
3. $\lfloor(9_s + 11_e) / 2\rfloor = 10$, 10은 10보다 작은가? X
    `max_v`는 건드리지 않고, $e$를 10-1인 9로 생긴
4. $\lfloor(9_s + 9_e) / 2\rfloor = 9$, 9는 10보다 작은가? O
    현재 `max_v` (8) 보다 9가 크므로 `max_v`를 9로 갱신, $s$는 9+1인 10으로 갱신
5. $10_s$가 $9_e$보다 커졌으므로 그만둠
최종적으로 나온 `max_v`의 값 9가 해당 최댓값 구하는 최적화 문제의 답이 된다.

이것을 파라메트릭 서치라고 한다.  

스터디할 때 살펴본 링크
https://beta.velog.io/@doorbals_512/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%8C%8C%EB%9D%BC%EB%A9%94%ED%8A%B8%EB%A6%AD-%EC%84%9C%EC%B9%98Parametric-Search
https://loosie.tistory.com/518
https://sarah950716.tistory.com/16

## 코드 해설

[코드](./code.py)

이 문제도 가장 가까운 공유기 사이의 거리가 최대 거리인 값을 찾는 최적화 문제이다.  

집 좌표 x의 범위가 0 ~ 1,000,000,000 으로 십억이고, 집의 개수 N은 20만개이므로  
$200,000* log10B$ 하면 600백만의 시간복잡도를 가지므로 집 좌표를 이분 탐색해 거리를 구하는 것을 예상할 수 있었다.  

` 14|arr.sort()` 먼저 집 위치를 정렬했는데 아래 로직들을 수행하기 위해서이다.  
먼저 C가 2개, 즉, 설치하는 공유기가 2개라면 이분탐색할 필요가 없고, 제일 큰 위치값과 제일 작은 위치값의 차이를 출력하면 되므로 if로 걸렀다

```python
# line 16
if C == 2:
    print(arr[-1] - arr[0])
    exit()
```

그 후 가장 인접한 집 사이 거리의 최댓값을 구하기 위한 이분 탐색을 위해,  
거리의 최솟값을 찾고 

```python
import math
...
# line 20
min_diff = math.inf
for i in range(len(arr) - 1):
    min_diff = min(min_diff, arr[i+1] - arr[i])
```

거리의 최댓값을 찾는다.

```python
s = min_diff # 최솟값을 s에 넣음

# line 52
e = (arr[-1] - arr[0]) // (C-1) # 최대거리를 공유기 수 (C-1)을 나눔
```

이 가장인접한 거리의 범위의 최솟값(`s`)과 최댓값(`e`)을 이용하여 중간 거리 `mid` 를 구하고,  
`mid` 거리를 가장 인접한 거리의 최솟값이라고 가정하여,  
공유기를 설치한 집들 사이 거리들이 이 `mid` 거리값 이상일 때  
C개의 공유기를 충분히 설치할 수 있을지 여부를 `is_installed_C_router` 함수로 계산해 받아온다.

```python
# line 54
while s <= e:
    mid = (s + e) // 2
    is_installed_enough = is_installed_C_router(arr, mid)
```

만약 충분히 설치가 됐다면, 가장 인접한 집 사이 거리값(`mid`)이 충분하다는 얘기이므로,  
거리 `mid` 의 크기를 키우고,  
충분히 설치가 안됐다면, 가장 인접한 집 사이 거리값이 크다는 얘기이므로,  
거리 `mid` 의 크기를 줄인다.  
이때 충분히 설치가 됐다면, 그때의 거리 `mid` 값들 중 가장 큰 값을 `max_min_dist` 에 넣는다.

```python
# line 54
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
```

함수 `is_installed_C_router`는 집 위치 배열과, 가장 인접한 집 사이 거리의 최댓값이라고 가정한 거리값이 들어온다.

```python
# line 27
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
```

가장 왼쪽에 위치한 집을 시작으로, 오른쪽 끝 집까지 공유기를 설치해나가는데, 변수 의미는 다음과 같다.  
- cnt: 공유기를 설치한 집 수를 의미한다.
- left_house_idx: 왼쪽 집부터 시작해서 거리 이상 떨어진 집에 공유기를 설치해나가는데,  
    현재 공유기를 설치한 집들 중 가장 왼쪽에 있는 집 인덱스, 
    즉, 집 위치값들이 들어있는 arr에서 마지막으로 공유기 설치한 집위치의 인덱스이다.

- i: 현재 공유기를 설치한 집의 다음으로 설치할 집의 인덱스를 가리킨다.
    만약에 현재 설치한 공유기의 집 위치값(`arr[left_house_idx]`)와 다음 집의 위치값(`arr[i]`)의 차,  
    즉, 현재 집과 다음 집과의 거리가 `dist`보다 크거나 같다면 공유기를 설치할 수 있으므로,
    마지막으로 공유기를 설치한 집의 인덱스를 저장하는 `left_house_idx`를 `i` 값으로 갱신하고,  
    공유기를 하나 더 설치했다는 의미로 `cnt`에 1을 더한다.

    만약에 현재 집과 다음 집과의 거리가 `dist`보다 작다면, `i`에 1을 더해 그 다음 집을 살펴보도록 한다.

시간복잡도는 `while s <= e` 이분탐색은 $O(logx)$ 로 $x$를 최댓값 10억이라고 잡으면 못해도 30번 이하로 실행하고,  
`is_installed_C_router` 은 $O(N)$ 으로 $N$을 최댓값 20만으로 잡으면 20만번 실행된다.  
총 30 * 200,000 으로 최악의 시간복잡도는 600만이 된다.