#Runtime: 24 ms, faster than 94.55% of Python3 online submissions for Convert a Number to Hexadecimal.
#Memory Usage: 14.3 MB, less than 44.61% of Python3 online submissions for Convert a Number to Hexadecimal.

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        digit = ''
        dic = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        while num != 0 and len(digit) < 8:
            remain = num%16
            num = (num - remain)//16
            if remain >= 10:
                digit = dic[remain] + digit
            else:
                digit = str(remain) + digit
        return digit
