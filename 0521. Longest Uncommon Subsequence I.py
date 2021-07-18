#Runtime: 24 ms, faster than 93.08% of Python3 online submissions for Longest Uncommon Subsequence I.
#Memory Usage: 14 MB, less than 98.62% of Python3 online submissions for Longest Uncommon Subsequence I.

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a != b:
            return max(len(a), len(b))
        return -1
