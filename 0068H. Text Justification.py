#Runtime: 28 ms, faster than 85.95% of Python3 online submissions for Text Justification.
#Memory Usage: 14.2 MB, less than 93.86% of Python3 online submissions for Text Justification.

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        cand = []
        temp = ''
        re = ''
        w_n = 0
        w_l = 0
        for i in words:
            if len(temp) + len(i) > maxWidth:
                if w_n-1 == 0:
                    temp = temp[:-1]
                    temp += ' '*(maxWidth-len(temp))
                    cand.append(temp)
                else:
                    all_n = (maxWidth-w_l)//(w_n-1)
                    part_n = (maxWidth-w_l)%(w_n-1)
                    part = temp.split(' ')
                    re = part[0]
                    for j in range(part_n):
                        re += ' '*(all_n+1) + part[j+1]
                    for j in range(w_n - 1 - part_n):
                        re += ' '*(all_n) + part[part_n + j + 1]
                    cand.append(re)
                temp = ''
                w_n = 0
                w_l = 0
            temp += i + " "
            w_n += 1
            w_l += len(i)
        temp = temp[:-1]
        temp += " "*(maxWidth-len(temp))
        cand.append(temp)
        return cand
