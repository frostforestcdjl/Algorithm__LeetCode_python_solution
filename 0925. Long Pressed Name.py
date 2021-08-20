#Runtime: 24 ms, faster than 96.79% of Python3 online submissions for Long Pressed Name.
#Memory Usage: 14.1 MB, less than 85.73% of Python3 online submissions for Long Pressed Name.

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n_i = t_i = 0
        while n_i < len(name):
            if t_i >= len(typed) or name[n_i] != typed[t_i]:
                return False
            elif n_i+1 == len(name) or name[n_i] != name[n_i+1]:
                while t_i+1 < len(typed) and typed[t_i+1] == name[n_i]:
                    t_i += 1
            n_i += 1
            t_i += 1
        if t_i != len(typed):
            return False
        return True
