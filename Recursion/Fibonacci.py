def fib(n: int, memo = {}):
    if n in memo:
        return memo[n]
    if n < 2:
        return n

    memo[n] = fib(n-1, memo) + fib(n-2,memo)
    return memo[n]



def climbStairs( n: int, memo = {}) -> int:
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return 1

    memo[n] = climbStairs(n - 1, memo) + climbStairs(n - 2, memo)

    return memo[n]

print(fib(800)/fib(799))