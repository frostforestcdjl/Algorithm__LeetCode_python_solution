#Runtime: 24 ms, faster than 97.55% of Python3 online submissions for Simplify Path.
#Memory Usage: 14.4 MB, less than 45.52% of Python3 online submissions for Simplify Path.

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
