N = int(input())
weights = list(map(int, input().split()))
M = int(input())
beads = list(map(int, input().split()))

cases = {0}
for weight in weights:
    new_cases = set(cases)
    for case in cases:
        new_cases.add(case - weight)
        new_cases.add(case + weight)
    cases = new_cases

res = ['Y' if bead in cases else 'N' for bead in beads]
print(*res)
