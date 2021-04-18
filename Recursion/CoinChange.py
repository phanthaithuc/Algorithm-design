from typing import List

def coinchange(coins: List[int], amount : int) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(amount + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], 1 + dp[a - coin])

    return dp[amount] if dp[amount] != amount else -1

print(coinchange([1,3,4,5], 7))