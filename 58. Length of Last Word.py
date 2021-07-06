class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        y = list(s)
        try:
            while (y[-1] == ' '):
                y.pop(-1)
        except:
            return 0

        for i in range (1, len(y)+1):
            if y[-i] == ' ':
                return len(y[-i+1:len(y)])
        return len(y)
