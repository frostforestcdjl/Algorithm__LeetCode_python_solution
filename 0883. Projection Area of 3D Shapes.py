#Runtime: 68 ms, faster than 86.64% of Python3 online submissions for Projection Area of 3D Shapes.
#Memory Usage: 14.2 MB, less than 94.58% of Python3 online submissions for Projection Area of 3D Shapes.

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = 0
        xz = 0
        yz_list = [0 for i in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    xy += 1
                if grid[i][j] > yz_list[j]:
                    yz_list[j] = grid[i][j]
            xz += max(grid[i])
        return xy + xz + sum(yz_list)
