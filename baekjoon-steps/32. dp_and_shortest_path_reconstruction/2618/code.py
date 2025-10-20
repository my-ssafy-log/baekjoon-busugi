N = int(input())
W = int(input())
works = [tuple(map(int, input().split())) for _ in range(W)]

def dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

memo = {}
cnt = 0

paths = []
def f(cur_work, pos1, pos2):
    global cnt
    if cur_work == len(works):
        return 0
    if (pos1, pos2, cur_work) in memo:
        return memo[(pos1, pos2, cur_work)]

    dist1 = dist(works[cur_work], pos1) + f(cur_work + 1, works[cur_work], pos2)
    dist2 = dist(works[cur_work], pos2) + f(cur_work + 1, pos1, works[cur_work])
    
    memo[(pos1, pos2, cur_work)] = min(dist1, dist2)
    return memo[(pos1, pos2, cur_work)]

min_dist = f(0, (1, 1), (N, N))
pos1, pos2 = (1, 1), (N, N)
for cur_work in range(W):
    dist1 = dist(works[cur_work], pos1) + f(cur_work + 1, works[cur_work], pos2)
    dist2 = dist(works[cur_work], pos2) + f(cur_work + 1, pos1, works[cur_work])

    if dist1 < dist2:
        pos1 = works[cur_work]
        paths.append(1)
    else:
        pos2 = works[cur_work]
        paths.append(2)

print(min_dist, *paths, sep='\n')

# 12 + 8
# 12 + 2
