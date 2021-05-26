import time
import functools
from typing import List
from collections import defaultdict


# def timeit(f):
#     is_evaluating = False
#
#     def g(*args, **kwargs):
#         nonlocal is_evaluating
#         if is_evaluating:
#             return f(*args, **kwargs)
#         else:
#             start_time = time.time()
#             is_evaluating = True
#             try:
#                 value = f(*args, **kwargs)
#             finally:
#                 is_evaluating = False
#             end_time = time.time()
#             print(f"Function {f.__name__}" + f" finished in: {end_time - start_time: .5f}" + " seconds")
#             return value
#
#     return g

def timeit(func):
    is_valuating = False

    def get_time(*args, **kwargs):
        nonlocal is_valuating
        if is_valuating:
            return func(*args, **kwargs)
        else:
            start = time.time()
            is_valuating = True
            try:
                output = func(*args, **kwargs)
            finally:
                is_valuating = False
            print(f"Function '{func.__name__}'" + f" finish in :{time.time() - start:.5f}" + " seconds")

            return output

    return get_time


@timeit
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


@timeit
def travel(r: int, c: int, memo={}) -> int:
    if (r, c) in memo:
        return memo[(r, c)]
    if r == 0 or c == 0:
        return 0
    if r == 1 and c == 1:
        return 1
    memo[(r, c)] = travel(r - 1, c, memo) + travel(r, c - 1, memo)
    return memo[(r, c)]


m, n = 58, 80
#(uniquePaths(m, n))
print((travel(m, n)))
