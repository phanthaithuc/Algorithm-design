from typing import List


def isPrime(nums: int) -> bool:
    if nums <=1 :
        return False
    if nums <= 3:
        return True

    for i in range(2, nums):
        if nums % i == 0:
            return False

    return True


def primes(n: int) -> List[int]:
    res = []
    for i in range(2, n + 1):
        if isPrime(i):
            res.append(i)

    return res


if __name__ == "__main__":
    print(primes(14))
