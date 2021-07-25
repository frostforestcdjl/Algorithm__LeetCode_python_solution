#Runtime: 124 ms, faster than 66.56% of Python3 online submissions for Valid Palindrome II.
#Memory Usage: 14.5 MB, less than 73.09% of Python3 online submissions for Valid Palindrome II.

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def no_quota(s):
            for i in range(len(s)//2):
                if s[i] != s[~i]:
                    return False
            return True
        s = '0' + s + '0'
        for i in range(len(s)//2):
            if s[i] != s[~i]:
                s_l = s[i+1:~i+1]
                s_r = s[i:~i]
                return no_quota(s_l) or no_quota(s_r)
        return True
