#Runtime: 720 ms, faster than 5.47% of Python3 online submissions for Longest Valid Parentheses.
#Memory Usage: 14.9 MB, less than 26.46% of Python3 online submissions for Longest Valid Parentheses.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l_s = len(s)
        digi = [i for i in range(len(s))]
        count = 0
        while '()' in s:
            index = s.index('()')
            s = s[:index] + s[index + 2:]
            digi = digi[:index] + digi[index + 2:]
        if not digi:
            return l_s
        digi_diff = [digi[0]]
        
        for i in range(1, len(digi)):
            digi_diff.append(digi[i] - digi[i-1] - 1)
        digi_diff.append(l_s - digi[-1] - 1)
        return max(digi_diff)
