#Runtime: 20 ms, faster than 99.70% of Python3 online submissions for Multiply Strings.
#Memory Usage: 14.2 MB, less than 81.36% of Python3 online submissions for Multiply Strings.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}
        sum_n1 = 0
        sum_n2 = 0
        for i in range(len(num1)):
            sum_n1 += dic[num1[~i]] * 10**i
        for i in range(len(num2)):
            sum_n2 += dic[num2[~i]] * 10**i
        mul = sum_n1*sum_n2
        return str(mul)
