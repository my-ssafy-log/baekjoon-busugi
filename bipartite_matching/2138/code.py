N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(1, N+1):
    arr = list(map(int, input().split()))[1:]
    graph[i].extend(arr)

c = [False] * (M+1)
d = [0] * (M+1)
def dfs(leftside):
    for rightside in graph[leftside]:
        if c[rightside]: continue
        c[rightside] = True
        if d[rightside] == 0 or dfs(d[rightside]):
            d[rightside] = leftside
            return True
    return False

for i in range(1, N+1):
    c = [False] * (M+1)
    # print(d)
    dfs(i)

print(sum([int(num > 0) for num in d]))