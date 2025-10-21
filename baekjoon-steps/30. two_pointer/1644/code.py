N = int(input())
sieve = [True] * (N + 1)
sieve[0] = sieve[1] = False

primes = []

for i in range(2, N+1):
    if not sieve[i]:
        continue
    primes.append(i)
    for j in range(i ** 2, N+1, i):
        sieve[j] = False

prefix_sum = 2
i = 0
j = 0

cnt = 0

while i <= j and primes:
    if prefix_sum == N:
        cnt += 1
        prefix_sum -= primes[i]
        i += 1
    elif prefix_sum < N:
        j += 1
        if j >= len(primes):
            break

        prefix_sum += primes[j]
    elif prefix_sum > N:
        prefix_sum -= primes[i]
        i += 1

print(cnt)
