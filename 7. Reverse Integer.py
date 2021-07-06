class Solution:
    def reverse(self, x: int) -> int:
        if (x < -2**31) or x > (2**31 - 1):
            return 0
        if x >= 0:
            w = list(str(x))[::-1]
            s = ''
            for i in w:
                s = s + str(i)
            if (int(s) < -2**31) or (int(s) > (2**31 - 1)):
                return 0
            return int(s)
        else:
            x = abs(x)
            w = list(str(x))[::-1]
            s = ''
            for i in w:
                s = s + str(i)
            if (-1*int(s) < -2**31) or (-1*int(s) > (2**31 - 1)):
                return 0
            return -1*int(s)
