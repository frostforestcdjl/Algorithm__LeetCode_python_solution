#Runtime: 496 ms, faster than 77.31% of Python3 online submissions for Island Perimeter.
#Memory Usage: 14.4 MB, less than 93.40% of Python3 online submissions for Island Perimeter.

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        side_n = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    if i == 0:
                        Top = 0
                    else:
                        Top = grid[i-1][j]
                    if i == len(grid) - 1: 
                        Butt = 0
                    else:
                        Butt = grid[i+1][j]
                    if j == 0:
                        Left = 0
                    else:
                        Left = grid[i][j-1]
                    if j == len(grid[0]) - 1: 
                        Right = 0
                    else:
                        Right = grid[i][j+1]
                    side_n = side_n + 4 - (Top + Butt + Left + Right)
        return side_n
