#Runtime: 112 ms, faster than 99.88% of Python3 online submissions for Set Matrix Zeroes.
#Memory Usage: 15 MB, less than 91.08% of Python3 online submissions for Set Matrix Zeroes.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        index_i = set()
        index_j = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    index_i.add(i)
                    index_j.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in index_i or j in index_j:
                    matrix[i][j] = 0
        return matrix
