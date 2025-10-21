n = int(input())

cnt = 0
def fib(n):
    global cnt
    if n == 1 or n == 2:
        cnt += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)
fib(n)
print(cnt, end=' ')


cnt = 0
f = [0] * 41
def fibonacci(n):
    global cnt
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        cnt += 1
        f[i] = f[i-1] + f[i-2]
fibonacci(n)
print(cnt)