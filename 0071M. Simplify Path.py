#Runtime: 32 ms, faster than 71.86% of Python3 online submissions for Simplify Path.
#Memory Usage: 14.1 MB, less than 90.67% of Python3 online submissions for Simplify Path.

class Solution:
    def simplifyPath(self, path: str) -> str:
        split = path.split('/')
        while '' in split:
            split.remove('')
        while '.' in split:
            split.remove('.')
        i = 0
        while i < len(split):
            if split[i] == '..':
                if i != 0:
                    split.pop(i-1)
                    split.pop(i-1)
                    i -= 1
                else:
                    split.pop(i)
            else:
                i += 1
        
        recomb = '/'.join(split)
        return '/' + recomb
