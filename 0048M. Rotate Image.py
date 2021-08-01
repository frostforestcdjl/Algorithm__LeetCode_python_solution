#Runtime: 36 ms, faster than 64.93% of Python3 online submissions for Rotate Image.
#Memory Usage: 14 MB, less than 95.62% of Python3 online submissions for Rotate Image.

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)//2):
            for j in range(i, len(matrix) - i - 1):
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]
        return matrix
