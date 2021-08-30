#Runtime: 8796 ms, faster than 5.00% of Python3 online submissions for 01 Matrix.
#Memory Usage: 17.4 MB, less than 49.65% of Python3 online submissions for 01 Matrix.

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        for i in range(len(mat)):
            mat[i] = [-1] + mat[i] + [-1]
        mat = [[-1 for i in range(len(mat[0]))]] + mat + [[-1 for i in range(len(mat[0]))]]
        stack_1 = []
        stack_2 = []
        stack_3 = []
        for i in range(1, len(mat)-1):
            for j in range(1, len(mat[0])-1):
                if mat[i][j] == 1 and mat[i-1][j]*mat[i+1][j]*mat[i][j-1]*mat[i][j+1] == 0:
                    stack_1.append([i,j])
        for cord in stack_1:
            i, j = cord[0], cord[1]
            if mat[i-1][j] == 1 and [i-1, j] not in stack_1:
                mat[i-1][j] = 2
                stack_2.append([i-1,j])
            if mat[i+1][j] == 1 and [i+1, j] not in stack_1:
                mat[i+1][j] = 2
                stack_2.append([i+1,j])
            if mat[i][j-1] == 1 and [i, j-1] not in stack_1:
                mat[i][j-1] = 2
                stack_2.append([i,j-1])
            if mat[i][j+1] == 1 and [i, j+1] not in stack_1:
                mat[i][j+1] = 2
                stack_2.append([i,j+1])
        k = 3
        while stack_2:
            for cord in stack_2:
                i, j = cord[0], cord[1]
                if mat[i-1][j] == 1 and [i-1, j] not in stack_1:
                    mat[i-1][j] = k
                    stack_3.append([i-1,j])
                if mat[i+1][j] == 1 and [i+1, j] not in stack_1:
                    mat[i+1][j] = k
                    stack_3.append([i+1,j])
                if mat[i][j-1] == 1 and [i, j-1] not in stack_1:
                    mat[i][j-1] = k
                    stack_3.append([i,j-1])
                if mat[i][j+1] == 1 and [i, j+1] not in stack_1:
                    mat[i][j+1] = k
                    stack_3.append([i,j+1])
            stack_2 = stack_3
            stack_3 = []
            k += 1
        mat = mat[1:-1]
        for i in range(len(mat)):
            mat[i] = mat[i][1:-1]
        return mat
