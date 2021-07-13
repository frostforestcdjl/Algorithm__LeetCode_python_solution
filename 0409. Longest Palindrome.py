#Runtime: 20 ms, faster than 99.65% of Python3 online submissions for Longest Palindrome.
#Memory Usage: 14.1 MB, less than 82.52% of Python3 online submissions for Longest Palindrome.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        set_s = set(s)
        length = 0
        odd = 0
        for i in set_s:
            if s.count(i)%2 == 0:
                length += s.count(i)
            else:
                length += s.count(i) - 1
                odd = 1
        return length + odd
