#Runtime: 36 ms, faster than 95.06% of Python3 online submissions for Unique Paths II.
#Memory Usage: 14.3 MB, less than 83.70% of Python3 online submissions for Unique Paths II.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) == 1 or len(obstacleGrid[0]) == 1:
            return 1 - max([max(obstacleGrid[i]) for i in range(len(obstacleGrid))])
        if obstacleGrid[0][0] == 1 or obstacleGrid[1][0] + obstacleGrid[0][1] == 2:
            return 0
        matri = [[1 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        for i in range(1, len(obstacleGrid)):
            if obstacleGrid[i][0] == 1 or matri[i-1][0] == 0:
                matri[i][0] = 0
        for i in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1 or matri[0][i-1] == 0:
                matri[0][i] = 0
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    matri[i][j] = 0
                else:
                    matri[i][j] = matri[i-1][j] + matri[i][j-1]
        return matri[-1][-1]
