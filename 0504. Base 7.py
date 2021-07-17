#Runtime: 28 ms, faster than 83.61% of Python3 online submissions for Base 7.
#Memory Usage: 14.2 MB, less than 69.48% of Python3 online submissions for Base 7.

class Solution:
    def convertToBase7(self, num: int) -> str:
        sign = ''
        if num < 0:
            sign = '-'
            num = abs(num)
        digit = ''
        while num >= 7:
            digit = str(num%7) + digit
            num = (num - num%7)//7
        digit = str(num%7) + digit
        return sign + digit
