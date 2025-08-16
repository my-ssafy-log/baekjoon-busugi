N = 11

_id = 0  # 고유 아이디
parents = [None] * (N+1)  # 방문 기록 및 부모 설정
finished = [False] * (N+1)
graph = [[] for _ in range(N+1)]
scc_list = []
stack = []

def dfs(node):
    global _id
    _id += 1
    parents[node] = _id
    stack.append(node)

    parent = parents[node]
    for child in graph[node]:
        if parents[child] is None:
            parent = min(parent, dfs(child))
        elif not finished[child]:
            parent = min(parent, parents[child])
    
    if parent == parents[node]:
        scc = []
        while True:
            child = stack.pop()
            scc.append(child)
            finished[child] = True
            if child == node:
                break
        scc_list.append(scc)
    
    return parent

v = 11
graph[1].append(2)
graph[2].append(3)
graph[3].append(1)
graph[4].append(2)
graph[4].append(5)
graph[5].append(7)
graph[6].append(5)
graph[7].append(6)
graph[8].append(5)
graph[8].append(9)
graph[9].append(10)
graph[10].append(11)
graph[11].append(8)
graph[11].append(3)

for node in range(1, N+1):
    if not finished[node]: dfs(node)

for i, scc in enumerate(scc_list):
    print(f"{i+1}번째 scc:", *scc)