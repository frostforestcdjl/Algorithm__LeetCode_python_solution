#Runtime: 80 ms, faster than 93.21% of Python3 online submissions for Surface Area of 3D Shapes.
#Memory Usage: 14.1 MB, less than 93.67% of Python3 online submissions for Surface Area of 3D Shapes.

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        xy = side = 0
        for i in range(len(grid)):
            grid[i] = [0] + grid[i]
        grid = [[0]*len(grid[0])] + grid
        for i in range(1, len(grid)):
            for j in range(1, len(grid)):
                if grid[i][j] != 0:
                    xy += 1
                side += max(grid[i][j] - grid[i-1][j], 0)
                side += max(grid[i][j] - grid[i][j-1], 0)
        return (side + xy)*2
