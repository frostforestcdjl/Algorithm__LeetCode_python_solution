#Runtime: 36 ms, faster than 82.18% of Python3 online submissions for Remove Outermost Parentheses.
#Memory Usage: 14.2 MB, less than 85.00% of Python3 online submissions for Remove Outermost Parentheses.

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        re = ''
        l = count = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            else:
                count -= 1
            if count == 0:
                re += s[l+1:i]
                l = i+1
        return re
 

#Runtime: 60 ms, faster than 10.91% of Python3 online submissions for Remove Outermost Parentheses.
#Memory Usage: 31.7 MB, less than 8.17% of Python3 online submissions for Remove Outermost Parentheses.
  
class Solution2:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        r = 0
        for i in range(len(s)):
            if s[i] == ')' and stack[-1] == '(':
                stack.pop(-1)
            else:
                stack.append(s[i])
            if not stack:
                s = s[1:i] + self.removeOuterParentheses(s[i+1:])
                break
        return s
