#Runtime: 80 ms, faster than 94.23% of Python3 online submissions for Reshape the Matrix.
#Memory Usage: 14.7 MB, less than 95.63% of Python3 online submissions for Reshape the Matrix.

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        if len(mat) == r:
            return mat
        int_mat = []
        for i in mat:
            int_mat += i            
        new = [[] for i in range(r)]
        k = 0
        for i in range(r):
            for j in range(c):
                new[i].append(int_mat[k])
                k += 1
        return new
