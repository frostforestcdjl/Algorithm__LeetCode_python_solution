#Runtime: 24 ms, faster than 97.60% of Python3 online submissions for Number of Lines To Write String.
#Memory Usage: 14.1 MB, less than 75.45% of Python3 online submissions for Number of Lines To Write String.

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        ls = 0
        ln = 1
        for i in s:
            if ls + widths[ord(i)-97] <= 100:
                ls += widths[ord(i)-97]
            else:
                ln += 1
                ls = widths[ord(i)-97]
        return ln, ls
