#Runtime: 20 ms, faster than 98.97% of Python3 online submissions for Reverse Only Letters.
#Memory Usage: 14.2 MB, less than 48.26% of Python3 online submissions for Reverse Only Letters.

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        r_list = []
        for i in s:
            if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
                r_list.append(i)
        r_list = r_list[::-1]
        for i in range(len(s)):
            if 65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122:
                s = s[:i] + r_list[0] + s[i+1:]
                r_list = r_list[1:]
        return s

      
#Runtime: 24 ms, faster than 95.48% of Python3 online submissions for Reverse Only Letters.
#Memory Usage: 14.2 MB, less than 48.26% of Python3 online submissions for Reverse Only Letters.
  
class Solution2:
    def reverseOnlyLetters(self, s: str) -> str:
        r_list = []
        l, r = 0, len(s) -1
        s = list(s)
        while l < r:
            if s[l].isalpha():
                if s[r].isalpha():
                    s[l], s[r] = s[r], s[l]
                    l += 1
                r -= 1
            else:
                l += 1
        return ''.join(s)
