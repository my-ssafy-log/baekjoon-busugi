from itertools import accumulate

T = int(input())

for t in range(T):
    N = int(input())
    cards = list(map(int, input().split()))

    cumulative_cards = [0] + list(accumulate(cards))

    memo = [[-1] * N for _ in range(N)]

    def f(s, e):
        if s == e:
            return cards[s]
        if memo[s][e] != -1:
            return memo[s][e]
        total = [
            cumulative_cards[e+1] - cumulative_cards[s+1],
            cumulative_cards[e] - cumulative_cards[s]
        ]
        memo[s][e] = max(
            cards[s] + total[0] - f(s + 1, e),
            cards[e] + total[1] - f(s, e - 1)
        )
        return memo[s][e]

    print(f(0, N-1))
