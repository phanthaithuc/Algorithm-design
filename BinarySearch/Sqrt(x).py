def sqrt(x: int) -> int:
    left, right = 0, x
    res = 0

    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x:
            left = mid + 1
            res = mid
        else:
            right = mid - 1

    return res


print(sqrt(12))