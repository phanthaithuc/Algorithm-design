def fib(n, memo={}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

    return memo[n]


def fin(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 2:
        return 1

    return fib(n - 1) + fib(n - 2)


def golden_ratio(n, memo):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 3

    if n in memo:
        return memo[n]

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

    return memo[n]


print(fib(250) / 250)
