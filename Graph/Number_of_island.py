from typing import List


class Solution(object):
    # def inrange(self, gird, r, c):
    #     numRow, numCol = len(grid), len(grid[0])
    #     if r < 0 or c < 0 or r >= numRow or c >= numCol:
    #         return False
    #     return True

    def mark_visited(self, x: int, y: int, row: int, columns: int, grid: List[List[str]]):
        # if x = 0 or y = 0 (water) or x > row or y > columns (out of grid) or grid[x][y] != 1(already visited)
        # return
        if x < 0 or y < 0 or x >= row or y >= columns or grid[x][y] != "1":
            return

        grid[x][y] = 2

        self.mark_visited(x - 1, y, row, columns, grid)  # UP
        self.mark_visited(x + 1, y, row, columns, grid)  # DOWN
        self.mark_visited(x, y + 1, row, columns, grid)  # RIGHT
        self.mark_visited(x, y - 1, row, columns, grid)  # LEFT

    def number_of_island(self, grid: List[List[str]]) -> int:
        row = len(grid)
        if row == 0:
            return
        columns = len(grid[0])
        number_of_island = 0

        for current_row in range(row):
            for current_columns in range(columns):
                if grid[current_row][current_columns] == "1":
                    self.mark_visited(current_row, current_columns, row, columns, grid)
                    number_of_island += 1

        return number_of_island


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid:
        return 0

    m = len(grid)
    n = len(grid[0])
    sum = 0

    for i in range(m):
        for j in range(n):

            if grid[i][j] == "0":
                continue
            else:

                # sum up only once per chance of meeting "1"
                sum += 1
                stack = list()
                stack.append([i, j])

                # visit each "1" in the adjacent area using a stack
                while len(stack) != 0:

                    [p, q] = stack.pop()

                    if p >= 1 and grid[p - 1][q] == "1":
                        stack.append([p - 1, q])

                    if p < m - 1 and grid[p + 1][q] == "1":
                        stack.append([p + 1, q])

                    if q >= 1 and grid[p][q - 1] == "1":
                        stack.append([p, q - 1])

                    if q < n - 1 and grid[p][q + 1] == "1":
                        stack.append([p, q + 1])

                    # mark as visited
                    grid[p][q] = "0"

    return sum


grid1 = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(Solution().number_of_island(grid))