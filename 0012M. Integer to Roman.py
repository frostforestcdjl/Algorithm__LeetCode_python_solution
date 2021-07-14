#Runtime: 32 ms, faster than 99.59% of Python3 online submissions for Integer to Roman.
#Memory Usage: 14.2 MB, less than 82.59% of Python3 online submissions for Integer to Roman.

class Solution:
    def intToRoman(self, num: int) -> str:
        list_n = list(str(num))
        list_n = ['0']*(4-len(list_n)) + list_n
        d_1 = {'0':'', '1':'I', '2':'II', '3':'III', '4':'IV', '5':'V', '6':'VI', '7':'VII', '8':'VIII', '9':'IX'}
        d_2 = {'0':'', '1':'X', '2':'XX', '3':'XXX', '4':'XL', '5':'L', '6':'LX', '7':'LXX', '8':'LXXX', '9':'XC'}
        d_3 = {'0':'', '1':'C', '2':'CC', '3':'CCC', '4':'CD', '5':'D', '6':'DC', '7':'DCC', '8':'DCCC', '9':'CM'}
        d_4 = {'0':'', '1':'M', '2':'MM', '3':'MMM'}
        
        return d_4[list_n[0]] + d_3[list_n[1]] + d_2[list_n[2]] + d_1[list_n[3]]
