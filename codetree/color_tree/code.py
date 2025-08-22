Q = int(input())
quests = [tuple(map(int, input().split())) for _ in range(Q)]

class Node:
    def __init__(self, mid, pid, color, max_depth):
        self.mid = mid
        self.pid = pid
        self.color = color
        self.max_depth = max_depth
        self.subnodes = []  # 서브트리의 모든 노드
        self.children = []  # 바로 아래 자식 노드

roots = []
nodes = [None] * (int(1e5)+1)

def dfs(mid):
    colors = set()
    value = 0
    for child in nodes[mid].children:
        cvalue, ccolors = dfs(child)
        value += cvalue
        colors |= ccolors

    colors.add(nodes[mid].color)
    value += len(colors) ** 2
    return value, colors

for quest in quests:
    command, *args = quest
    if command == 100:
        mid, pid, color, max_depth = args
        node = Node(*args)
        nodes[mid] = node
        if pid == -1:
            roots.append(mid)
        else:  # 루트가 아니라면
            # 루트까지 올라가면서 max_depth 확인하며 추가할 수 있는지 체크
            cur_pid = pid
            need_depth = 2
            overflow = False
            while cur_pid != -1:
                if nodes[cur_pid].max_depth < need_depth:
                    overflow = True
                    break
                need_depth += 1
                cur_pid = nodes[cur_pid].pid

            if overflow:  # overflow 나면 무시
                continue

            nodes[pid].children.append(mid)

            cur_pid = pid
            # 부모부터 루트까지 서브노드에 mid를 추가함
            while cur_pid != -1:
                nodes[cur_pid].subnodes.append(mid)
                cur_pid = nodes[cur_pid].pid

    if command == 200:
        mid, color = args
        nodes[mid].color = color
        for subid in nodes[mid].subnodes:
            nodes[subid].color = color
    if command == 300:
        mid, = args
        print(nodes[mid].color)
    if command == 400:
        total = 0
        for rid in roots:
            value, _ = dfs(rid)
            total += value
        print(total)
