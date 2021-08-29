#Runtime: 20 ms, faster than 99.82% of Python3 online submissions for Valid Number.
#Memory Usage: 14.3 MB, less than 31.25% of Python3 online submissions for Valid Number.

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.replace('E', 'e')
        if s[0] == 'e' or s[-1] == 'e' or s[-1] == '+' or s[-1] == '-':
            return False
        text = list(s)
        sign_l = {'.', '+', '-', 'e'}
        num_l = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        n_check = False
        for i in text:
            if i not in num_l and i not in sign_l:
                return False
            if i in num_l:
                n_check = True
        if n_check == False:
            return False
        if s.count('e') > 1 or s.count('.') > 1:
            return False
        if 'e' in s and '.' in s:
            if s.index('.') > s.index('e') or (s.index('.') + 1 == s.index('e') and s.index('.') == 0):
                return False
        if s.count('+') + s.count('-') > 2:
            return False
        if s.count('+') == 1:
            if s.count('e') == 1:
                if s.index('+') != 0 and s.index('+') != s.index('e') + 1 or s.index('+') == s.index('e') - 1:
                    return False
            else:
                if s.index('+') != 0:
                    return False
        elif s.count('+') == 2:
            if s.count('e') != 1:
                return False
            else:
                if s.index('+') != 0 or s[s.index('e')+1] != '+':
                    return False
        if s.count('-') == 1:
            if s.count('e') == 1:
                if s.index('-') != 0 and s.index('-') != s.index('e') + 1 or s.index('-') == s.index('e') - 1:
                    return False
            else:
                if s.index('-') != 0:
                    return False
        elif s.count('-') == 2:
            if s.count('e') != 1:
                return False
            else:
                if s.index('-') != 0 and s[s.index('e')+1] != '-':
                    return False
        return True
