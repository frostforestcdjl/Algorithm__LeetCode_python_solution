#Runtime: 20 ms, faster than 99.22% of Python3 online submissions for Valid Parentheses.
#Memory Usage: 14.3 MB, less than 34.39% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if stack:
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return not stack


#Runtime: 2205 ms, faster than 5.48% of Python3 online submissions for Valid Parentheses.
#Memory Usage: 14.2 MB, less than 63.51% of Python3 online submissions for Valid Parentheses.
    
class Solution2:
    def isValid(self, s: str) -> bool:
        x = list(s)
        y = 0
        while (y != len(x)):
            y = len(x)
            for i in range(len(x)-1):
                try:
                    if (x[i] == '(') and (x[i+1] == ')'):
                        x.pop(i)
                        x.pop(i)
                    if (x[i] == '{') and (x[i+1] == '}'):
                        x.pop(i)
                        x.pop(i)
                    if (x[i] == '[') and (x[i+1] == ']'):
                        x.pop(i)
                        x.pop(i)
                except:
                    pass    
        if len(x) != 0:
            return False
        return True
