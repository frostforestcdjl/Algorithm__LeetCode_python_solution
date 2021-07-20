#Runtime: 112 ms, faster than 26.95% of Python3 online submissions for Valid Sudoku.
#Memory Usage: 14 MB, less than 99.79% of Python3 online submissions for Valid Sudoku.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            for j in range(9):
                if i.count(str(j+1)) > 1:
                    return False
        flip = []
        for i in range(9):
            temp = []
            for j in range(9):
                 temp.append(board[j][i])
            flip.append(temp)
        for i in flip:
            for j in range(9):
                if i.count(str(j+1)) > 1:
                    return False
        well = []
        for k in range(9):
            temp = []
            for i in range(3*(k//3), 3*(k//3) + 3):
                for j in range(3*(k%3), 3*(k%3) + 3):
                    temp.append(board[i][j])
            well.append(temp)
        for i in well:
            for j in range(9):
                if i.count(str(j+1)) > 1:
                    return False
        return True
