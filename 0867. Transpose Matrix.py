#Runtime: 64 ms, faster than 95.95% of Python3 online submissions for Transpose Matrix.
#Memory Usage: 14.8 MB, less than 64.62% of Python3 online submissions for Transpose Matrix.

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        trm = [[] for i in range(len(matrix[0]))]
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                trm[i].append(matrix[j][i])
        return trm
