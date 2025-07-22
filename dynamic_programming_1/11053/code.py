n = int(input())

arr = [0] + list(map(int, input().split()))

d = []

for i, cur in enumerate(arr):
    len_arr = []

    for j, dv in enumerate(arr[:i]):
        if dv < cur:
            len_arr.append(d[j])

    if len(len_arr) == 0:
        d.append(0)
    else:
        d.append(max(len_arr) + 1)
print(max(d))