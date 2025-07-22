n = int(input())

arr = [0] + list(map(int, input().split()))

d = []
reversed_d = []

for i, cur in enumerate(arr):
    len_arr = []

    for j, dv in enumerate(arr[:i]):
        if dv < cur:
            len_arr.append(d[j])

    if len(len_arr) == 0:
        d.append(0)
    else:
        d.append(max(len_arr) + 1)

reversed_arr = [0] + list(reversed(arr[1:]))

for i, cur in enumerate(reversed_arr):
    len_arr = []

    for j, dv in enumerate(reversed_arr[:i]):
        if dv < cur:
            len_arr.append(reversed_d[j])

    if len(len_arr) == 0:
        reversed_d.append(0)
    else:
        reversed_d.append(max(len_arr) + 1)

d = d[1:]
rereversed_d = list(reversed(reversed_d[1:]))

# print(arr[1:])
# print(d)
# print(arr[1:])
# print(rereversed_d)
print(max([d[i] + rereversed_d[i] for i in range(len(d))]) - 1)