#Runtime: 684 ms, faster than 5.08% of Python3 online submissions for Surrounded Regions.
#Memory Usage: 15.2 MB, less than 99.89% of Python3 online submissions for Surrounded Regions.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) <= 2 or len(board[0]) <= 2:
            return board
        stack = []
        save = []
        for i in range(len(board)):
            if board[i][0] == "O":
                stack.append([i,0])
            if board[i][-1] == "O":
                stack.append([i,len(board[0])-1])
        for i in range(len(board[0])):
            if board[0][i] == "O":
                stack.append([0,i])
            if board[-1][i] == "O":
                stack.append([len(board)-1,i])
        while stack:
            i, j = stack[0][0], stack[0][1]
            if i > 0 and board[i-1][j] == "O" and [i-1,j] not in stack and [i-1,j] not in save:
                stack.append([i-1,j])
            if i < len(board)-1 and board[i+1][j] == "O" and [i+1,j] not in stack and [i+1,j] not in save:
                stack.append([i+1,j])
            if j > 0 and board[i][j-1] == "O" and [i,j-1] not in stack and [i,j-1] not in save:
                stack.append([i,j-1])
            if j < len(board[0])-1 and board[i][j+1] == "O" and [i,j+1] not in stack and [i,j+1] not in save:
                stack.append([i,j+1])
            save.append(stack.pop(0))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if [i,j] not in save:
                    board[i][j] = "X"
