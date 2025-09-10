# 2696 중앙값 구하기

[링크](https://www.acmicpc.net/problem/2696)

## 문제 해설
이 문제는 최소 1개부터 최대 9999개의 나열되어 있는 수들이 있고, 첫번째 숫자부터 시작해서 빈 배열에 넣는다고 했을 때,  
그 배열의 길이가 홀수일 때 그 배열 내 수들 중 중앙값을 구하는 문제이다.

## 코드 해설
먼저 1번째로 들어오는 숫자가 출력이 되고, 그 후에 들어오는 2개의 숫자 이후 3번째 숫자가 출력이 되는데,  
이 2개의 숫자와 1번째 숫자와의 대소 관계에 대해 생각하며 구현해보았다.  

1번째로 들어오는 숫자는 1개니깐 무조건 출력하고, 1번째 숫자를 기준값(pivot)으로 설정한다.  
그 후에 들어오는 2개의 숫자는  
기준값보다 크거나 같다면 `기준값보다 크거나 같은 숫자들로 이루어진 최소힙큐(gte_hq)`에 추가되고,  
기준값보다 작다면 `기준값보다 작은 숫자들로 이루어진 최대힙큐(lt_hq)`에 추가된다.  

그러면서 `gte_hq`에 추가된 횟수, `lt_hq`에 추가된 횟수를 `gte`, `lt` 변수를 두어 추가로 카운트 한다.  


```python
# 31번째 줄
if arr[i] >= pivot:
    gte += 1
    heappush(gte_hq, arr[i])
else:
    lt += 1
    heappush(lt_hq, -arr[i])
```
1. 만약 `gte`와 `lt`가 같다면 중앙값은 변하지 않으므로 기준값, `pivot`을 건드리지 않는다.  
2. 만약 `gte`가 `lt`보다 크다면 중앙값은 `gte_hq` 최소힙큐에서 가장 앞쪽에 위치한 최소값이 되므로,  
    `lt_hq` 최대힙큐에 `pivot` 값을 추가하고 `pivot`에 `gte_hq.pop()` 한 값으로 갱신한다.
3. 만약 `gte`가 `lt`보다 작다면 중앙값은 `lt_hq` 최대힙큐에서 가장 앞쪽에 위치한 최대값이 되므로,
    `gte_hq` 최소힙큐에 `pivot` 값을 추가하고 `pivot`에 `lt_hq.pop()` 한 값으로 갱신한다.

출력결과를 담는 `res`에 중앙값을 유지하는 `pivot`을 추가하고 `gte`와 `lt`를 0으로 초기화해줬다.


```python
# 38번째 줄
if i % 2 == 1:
    if gte == lt:
        pass
    elif gte > lt:  # gte가 2, lt가 0일 때
        heappush(lt_hq, -pivot)
        pivot = heappop(gte_hq)
    else:  # gte가 0, lt가 2일 때
        heappush(gte_hq, pivot)
        pivot = -heappop(lt_hq)

    res.append(pivot)

    gte = 0
    lt = 0
```