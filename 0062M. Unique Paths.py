#Runtime: 24 ms, faster than 96.54% of Python3 online submissions for Unique Paths.
#Memory Usage: 14.2 MB, less than 66.85% of Python3 online submissions for Unique Paths.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matri = [[1]*n]*m
        for i in range(1, len(matri)):
            for j in range(1, len(matri[0])):
                matri[i][j] = matri[i][j-1] + matri[i-1][j]
        return matri[-1][-1]
