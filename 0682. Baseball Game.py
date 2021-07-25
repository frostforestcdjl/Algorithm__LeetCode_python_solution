#Runtime: 32 ms, faster than 96.18% of Python3 online submissions for Baseball Game.
#Memory Usage: 14.3 MB, less than 73.25% of Python3 online submissions for Baseball Game.

class Solution:
    def calPoints(self, ops) -> int:
        num_list = []
        for i in ops:
            if i == '+':
                num_list.append(num_list[-1] + num_list[-2])
            elif i == 'D':
                num_list.append(num_list[-1]*2)
            elif i == 'C':
                num_list.pop()
            else:
                num_list.append(int(i))
        return sum(num_list)
