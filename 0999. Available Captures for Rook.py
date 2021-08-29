#Runtime: 20 ms, faster than 99.44% of Python3 online submissions for Available Captures for Rook.
#Memory Usage: 14.1 MB, less than 97.21% of Python3 online submissions for Available Captures for Rook.

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        count = 0
        for i in range(len(board)):
            if 'R' in board[i]:
                r_cord = [i, board[i].index('R')]
                break
        for i in range(r_cord[0]):
            if board[r_cord[0]-i-1][r_cord[1]] == 'p':
                count += 1
                break
            if board[r_cord[0]-i-1][r_cord[1]] == 'B':
                break
        for i in range(len(board)-r_cord[0]-1):
            if board[r_cord[0]+i+1][r_cord[1]] == 'p':
                count += 1
                break
            if board[r_cord[0]+i+1][r_cord[1]] == 'B':
                break
        for i in range(r_cord[1]):
            if board[r_cord[0]][r_cord[1]-i-1] == 'p':
                count += 1
                break
            if board[r_cord[0]][r_cord[1]-i-1] == 'B':
                break
        for i in range(len(board)-r_cord[1]-1):
            if board[r_cord[0]][r_cord[1]+i+1] == 'p':
                count += 1
                break
            if board[r_cord[0]][r_cord[1]+i+1] == 'B':
                break
        return count
