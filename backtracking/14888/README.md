# 14888 연산자 끼워넣기

[링크](https://www.acmicpc.net/problem/14888)

## 문제 해설

연산자 끼워넣기 문제는 순서가 있는 나열된 수 사이에 주어진 연산자를 끼워넣어 최댓값과 최솟값을 구하는 문제이다.  
연산자에는 `+`, `-`, `*`, `/`가 있는데 여기서 `/`의 작동 방식을 유의해야한다.  
`/`는 **몫**만을 취하는데 만약 나뉘는 수가 만약 음수라면, 양수로 바꾸로 나눈 뒤 음수로 바꾼다.  
예시를 들면 `-1 / 3`에 `/`는

1. 먼저 `-1`을 양수로 바꿔 `1`로 만들고 (`1 / 3`)
2. `/ 3`을 수행한 뒤 (`1 / 3` = `0`)
3. 부호를 다시 음수로 바꾼다. (`0`)

최종적으로 `-1 / 3`의 실제 수학적 몫인 `-1`이 아니라 위의 과정으로 나온 `0`이 몫이 되는 것이다.  
(이 부분을 진짜 유의해야한다. 단순히 `a // b`를 수행하면 안된다)

또다른 유의사항은 수들은 연산자 우선순위와 상관없이 앞에 있는 수들부터 계산을 한다.  

예를 들어 `1 2 3 4 5 6`이라는 수들이 있고, `+`가 2개, `-`가 1개, `*`가 1개, `/`가 1개라면  
제일 큰 수를 만드는 식은 `1 - 2 / 3 + 4 + 5 * 6`으로 과정을 보면

1. 1 - 2 = -1
2. -1 / 3 = 0
3. 0 + 4 = 4
4. 4 + 5 = 9
5. 9 * 6 = 54

로 앞에서부터 계산해 최댓값인 54가 나온다.

문제의 출력은 이렇게 연산자를 끼워넣어 계산을 했을 때 최댓값과 최솟값을 출력하는 문제이다.

## 코드 해설

전체코드는 [code.py](./code.py)에 나와있다.

먼저 수의 개수와 나열되는 수를 입력받아 `n`아 `arr`변수에 넣는다.  

그 다음에 차례대로 `+`의 개수, `-`의 개수 `*`의 개수, `/`의 개수를 입력받고 각각을 `op_map` 딕셔너리에 담는다.  

또한 추가로 `for`문으로 반복을 돌릴 연산자 리스트도 `op_list`에 만들어둔다.  

max_v, min_v에는 각각 문제에서 밝히 가장 작은 값과 큰 값을 넣는다.

메인 코드는 `find_min_max`와 제일 아래의 `for`(이하 `for(1)`)문이다. 먼저 `for(1)`에서 첫번째로 놓을 연산자를 `op_list`에서 돌면서 반복하고, `if`문에서 해당하는 연산자가 사용할만큼 개수가 있는지 `op_map[op]`에서 확인을 한다.  
만약 사용할 수 있다면 `op_map[op]`에서 사용한다는 의미로 1을 빼고 `find_min_max()` 재귀함수를 돌린다.

`find_min_max()`함수는 각각의 인자로 `op_param`, `step`, `total`을 받는데 이 인자의 의미는 `total`을 `step`번째에 있는 숫자로 `op_param` 연산자를 수행한다는 의미이다.  
이 `total`을 `step-1`까지 연산을 수행해 나온 값을 의미해서 `find_min_max()`는 다음 작업을 실행한다.

```py
calc_total = get_calc_total(op_param, step, total)

if step == n - 1:
    # print(f"calc_total: {calc_total}")
    if max_v < calc_total: max_v = calc_total
    if min_v > calc_total: min_v = calc_total

for op in op_list:
    if op_map[op] > 0:
        op_map[op] -= 1
        find_min_max(op, step + 1, calc_total)
        op_map[op] += 1
```

`get_calc_total`은 연산자와 `total`, `step`을 받아 `total`에서 `step`을 이용해 연산자를 수행한 결과를 반환한다.  

```py
def get_calc_total(op, step, total):
    if op == '+': return total + arr[step]
    if op == '-': return total - arr[step]
    if op == '*': return total * arr[step]
    if op == '/': return total // arr[step] if total >= 0 else (-total) // arr[step] * -1
```
여기서 `total`이 음수라면 위에 말한 유의사항대로 연산 과정을 수행하는 것이 이 함수의 킥이다.

여기서 `step`이 `n-1`로 마지막 요소까지 도달했다면 최종적으로 계산된 값이 최댓값인지 최솟값인지 판단하여 각각 `max_v`, `min_v`에 대입한다.

만약 `step`이 `n-1`에 도달하지 않았다면 아직 계산할 수와 연산자가 남아있다는 의미이므로 아래에 `for`(이하`for(2)`)문을 수행한다.

```py
print(max_v)
print(min_v)
```

최종적으로 `for(1)`이 끝난 후 최댓값, 최솟값을 출력을 한다.