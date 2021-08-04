#Runtime: 36 ms, faster than 95.27% of Python3 online submissions for Search a 2D Matrix.
#Memory Usage: 14.7 MB, less than 86.50% of Python3 online submissions for Search a 2D Matrix.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i_index = -2
        if target > matrix[-1][-1]:
            return False
        for i in range(len(matrix)):
            if target == matrix[i][0]:
                return True
            if target < matrix[i][0]:
                i_index = i - 1
                break
        if i_index == -2:
            i_index = len(matrix) - 1
        if i_index == -1:
            return False
        for i in range(len(matrix[0])):
            if target == matrix[i_index][i]:
                return True
            if target < matrix[i_index][i]:
                return False
        return False
