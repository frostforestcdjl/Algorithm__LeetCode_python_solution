#Runtime: 74 ms, faster than 32.35% of Python3 online submissions for Evaluate Reverse Polish Notation.
#Memory Usage: 14.4 MB, less than 96.27% of Python3 online submissions for Evaluate Reverse Polish Notation.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '-':
                stack.append(-stack.pop() + stack.pop())
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '/':
                n2 = stack.pop()
                stack.append(int(stack.pop()/n2))
            else:
                stack.append(int(i))
        return stack[0]
