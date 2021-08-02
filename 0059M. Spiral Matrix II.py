#Runtime: 32 ms, faster than 67.73% of Python3 online submissions for Spiral Matrix II.
#Memory Usage: 14.1 MB, less than 92.73% of Python3 online submissions for Spiral Matrix II.

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matr = [[1 for i in range(n)] for i in range(n)]
        frame = [0, n-1, n-1, 0]
        direct = 'r'
        x = 0
        y = 0
        for i in range(1, n**2):
            if direct == 'r':
                if x != frame[1]:
                    x += 1
                else:
                    direct = 'd'
                    y += 1
                    frame[0] += 1
            elif direct == 'd':
                if y != frame[2]:
                    y += 1
                else:
                    direct = 'l'
                    x -= 1
                    frame[1] -= 1
            elif direct == 'l':
                if x != frame[3]:
                    x -= 1
                else:
                    direct = 'u'
                    y -= 1
                    frame[2] -= 1
            elif direct == 'u':
                if y != frame[0]:
                    y -= 1
                else:
                    direct = 'r'
                    x += 1
                    frame[3] += 1       
            matr[y][x] = i+1
        return matr
