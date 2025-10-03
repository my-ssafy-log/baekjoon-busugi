from collections import defaultdict

def set_comb_hist(ni, total, arr, hist):
    if ni == len(arr):
        hist[total] += 1
        return
    set_comb_hist(ni+1, total, arr, hist)
    set_comb_hist(ni+1, total+arr[ni], arr, hist)

def get_cumulative_sum(items):
    cumulsums = []
    cursum = 0
    for comb, cnt in items:
        cursum += cnt
        cumulsums.append((comb, cursum))
    return cumulsums

N, C = map(int, input().split())
arr = list(map(int, input().split()))
left = arr[:N//2]
right = arr[N//2:]

left_hist = defaultdict(int)
right_hist = defaultdict(int)

set_comb_hist(0, 0, left, left_hist)
set_comb_hist(0, 0, right, right_hist)

# 제일 조합이 많은 집합에서 이분탐색을 하기 위해 변수 설정
lhist_items = sorted(left_hist.items())
rhist_items = sorted(right_hist.items())
longest_items = lhist_items
shortest_items = rhist_items

if len(longest_items) < len(shortest_items):
    longest_items, shortest_items = shortest_items, longest_items

longest_cumulsums = get_cumulative_sum(longest_items)

def search(items, comb):
    s = 0
    e = len(items) - 1

    max_idx = 0
    while s <= e:
        m = (s + e) // 2
        if items[m][0] > comb:
            e = m - 1
        else:
            max_idx = max(max_idx, m)
            s = m + 1
    return max_idx

total_cnt = 0
for comb, cnt in shortest_items:
    if comb > C:
        break
    max_idx = search(longest_cumulsums, C - comb)
    total_cnt += cnt * longest_cumulsums[max_idx][1]
print(total_cnt)

"""
1073741824

"""
