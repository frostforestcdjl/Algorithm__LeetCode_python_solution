#Runtime: 20 ms, faster than 99.24% of Python3 online submissions for Spiral Matrix.
#Memory Usage: 14 MB, less than 95.03% of Python3 online submissions for Spiral Matrix.

class Solution:
    def spiralOrder(self, matrix):
        i = 0
        j = 0
        list_n = []
        direct = 'r'
        frame = [0, len(matrix[0]) - 1, len(matrix) - 1, 0]
        while frame[2] - frame[0] >= 0 and frame[1] - frame[3] >= 0:
            list_n.append(matrix[i][j])
            if direct == 'r':
                if j != frame[1]:
                    j += 1
                else:
                    direct = 'd'
                    i += 1
                    frame[0] += 1
            elif direct == 'd':
                if i != frame[2]:
                    i += 1
                else:
                    direct = 'l'
                    j -= 1
                    frame[1] -= 1
            elif direct == 'l':
                if j != frame[3]:
                    j -= 1
                else:
                    direct = 'u'
                    i -= 1
                    frame[2] -= 1
            elif direct == 'u':
                if i != frame[0]:
                    i -= 1
                else:
                    direct = 'r'
                    j += 1
                    frame[3] += 1
        return list_n
