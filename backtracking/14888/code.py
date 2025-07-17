n = int(input())
arr = list(map(int, input().split()))
max_v = -1000000000
min_v = 1000000000

plus, minus, mul, div = map(int, input().split())
op_list = ['+', '-', '*', '/']
op_map = {
    '+': plus,
    '-': minus,
    '*': mul,
    '/': div
}

def get_calc_total(op, step, total):
    if op == '+': return total + arr[step]
    if op == '-': return total - arr[step]
    if op == '*': return total * arr[step]
    if op == '/': return total // arr[step] if total >= 0 else (-total) // arr[step] * -1

def find_min_max(op_param, step, total = 0):
    global max_v, min_v
    # print(f"{op_param}, step:{step}, total: {total}")
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

for op in op_list:
    if op_map[op] > 0:
        op_map[op] -= 1
        find_min_max(op, 1, arr[0])
        op_map[op] += 1

print(max_v)
print(min_v)