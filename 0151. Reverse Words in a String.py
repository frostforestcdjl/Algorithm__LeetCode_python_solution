#Runtime: 28 ms, faster than 89.39% of Python3 online submissions for Reverse Words in a String.
#Memory Usage: 14.1 MB, less than 96.36% of Python3 online submissions for Reverse Words in a String.

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
