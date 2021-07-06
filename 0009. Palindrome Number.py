class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = list(str(x))
        z = y[::-1]
        for i in range(round(len(y)/2)):
            if y[i] != z[i]:
                return False
        return True
