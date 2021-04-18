from typing import List


def coinchange(coins: List[int], target: int) -> int:
    res = [target + 1] * (target + 1)
    res[0] = 0

    for i in range(1, target + 1):
        for coin in coins:
            if i - coin >= 0:
                res[i] = min(res[i], 1 + res[i - coin])

    return res[target] if res[target] != target else -1


print(coinchange([1,2,3], 7))