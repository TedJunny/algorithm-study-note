from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        sum = 0
        new_grid = list(map(list, zip(*grid)))

        for r in range(len(grid)):
            row_max = max(grid[r])
            for c in range(len(grid[r])):
                col_max = max(new_grid[c])
                sum += min(row_max, col_max) - grid[r][c]

        return sum


test = Solution()
print(
    test.maxIncreaseKeepingSkyline(
        [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    )
)
