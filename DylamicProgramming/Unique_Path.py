from typing import List
from collections import defaultdict


def uniquePaths(m: int, n: int) -> int:
    if m == 0 or n == 0:
        return 0
    if m == 1 or n == 1:
        return 1
    grid = [[0 for _ in range(n)] for _ in range(m)]
    grid[m - 1][n - 1] = 3
    x, y = 0, 0
    res = []

    def travel(x: int, y: int, grid: List[List[int]], memo=defaultdict(int)):
        if x > m - 1 or y > n - 1:
            return

        travel(x + 1, y, grid, memo)
        travel(x, y + 1, grid, memo)
        if grid[x][y] == 3:
            res.append([x, y])

    travel(x, y, grid)
    return len(res)


def travel(r: int, c: int, memo={}) -> int:
    if (r, c) in memo:
        return memo[(r, c)]
    if r == 0 or c == 0:
        return 0
    if r == 1 and c == 1:
        return 1
    memo[(r, c)] = travel(r - 1, c, memo) + travel(r, c - 1, memo)
    return memo[(r, c)]


m, n = 120, 120
print(uniquePaths(m, n))
print(travel(m, n))
