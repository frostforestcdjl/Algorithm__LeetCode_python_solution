#Runtime: 80 ms, faster than 91.92% of Python3 online submissions for Toeplitz Matrix.
#Memory Usage: 14.3 MB, less than 66.24% of Python3 online submissions for Toeplitz Matrix.

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        x = 0
        y = len(matrix) -1
        for i in range(len(matrix) + len(matrix[0]) - 1):
            k = 0
            try:
                while True:
                    if matrix[y + k][x + k] != matrix[y][x]:
                        return False
                    k += 1
            except:
                pass
            if y != 0:
                y -= 1
            else:
                x += 1
        return True
