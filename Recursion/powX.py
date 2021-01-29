def pow(x: float, n: int):
    if n == 0:
        return 1
    if x == 0:
        return 0
    if n < 0:
        return pow(1 / n, -n)
    if n % 2 == 1:
        return x * pow(x, n - 1)
    if n % 2 == 0:
        v = pow(x, n / 2)
        return v * v


def pow1(x: float, n: int):
    if n == 0:
        return 1

    if n > 0:
        power = x * pow1(x, n - 1)
    if n < 0:
        power = 1 / x * pow1(x, n + 1)
    return power


print(pow1(2, 6))

print(pow1(2, -6) == 2 ** (-6))
