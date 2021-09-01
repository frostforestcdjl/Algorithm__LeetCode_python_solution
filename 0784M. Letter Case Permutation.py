#Runtime: 52 ms, faster than 87.51% of Python3 online submissions for Letter Case Permutation.
#Memory Usage: 14.8 MB, less than 59.89% of Python3 online submissions for Letter Case Permutation.

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s = list(s)
        stack = []
        if s[0].isalpha():
            stack.append([s[0].upper(), 0])
            stack.append([s[0].lower(), 0])
        else:
            stack.append([s[0], 0])
        while stack:
            if stack[0][1]+1 == len(s):
                return list(zip(*stack))[0]
            pre, ind = stack.pop(0)
            if s[ind+1].isalpha():
                stack.append([pre + s[ind+1].upper(), ind+1])
                stack.append([pre + s[ind+1].lower(), ind+1])
            else:
                stack.append([pre + s[ind+1], ind+1])
