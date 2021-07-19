#Runtime: 28 ms, faster than 95.76% of Python3 online submissions for Generate Parentheses.
#Memory Usage: 14.8 MB, less than 11.22% of Python3 online submissions for Generate Parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        save = [[1]]
        for i in range(2*n-1):
            temp_len = len(save)
            for j in range(temp_len):
                if save[j].count(1) == n:
                    save[j].append(-1)
                elif sum(save[j]) == 0:
                    save[j].append(1)
                else:
                    save.append([] + save[j])
                    save[j].append(-1)
                    save[-1].append(1)
        dic = {1:'(', -1:')'}
        save_p = []
        for i in save:
            s = ''
            for j in i:
                s += dic[j]
            save_p.append(s)
        return save_p
