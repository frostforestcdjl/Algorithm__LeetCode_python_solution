#Runtime: 64 ms, faster than 99.27% of Python3 online submissions for Remove All Adjacent Duplicates In String.
#Memory Usage: 15.3 MB, less than 15.60% of Python3 online submissions for Remove All Adjacent Duplicates In String.

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
