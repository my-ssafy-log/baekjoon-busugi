T = int(input())
 
memo = [1, 1, 2, 6, 24, 120, 720]
def factorial(n):
    if len(memo)-1 >= n:
        return memo[n]
    memo.append(
        factorial(n-1) * n
    )
    return memo[n]
 
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    visited = [False] * (N)
 
    cnt = 0
    def dfs(step, left, right):
        global cnt
        # print(left, right)
        if step == N:
            cnt += 1
            # print(cnt)
            return
 
        if left >= total - left:
            cnt += (1 << (N - step)) * factorial(N - step)
            # print(cnt)
            return
         
        for i, elem in enumerate(arr):
            if visited[i]: continue
            visited[i] = True
            dfs(step+1, left + elem, right)
         
            if right + elem <= left:
                dfs(step+1, left, right + elem)
            visited[i] = False
 
    dfs(0, 0, 0)
    print(f"#{t+1}", cnt)