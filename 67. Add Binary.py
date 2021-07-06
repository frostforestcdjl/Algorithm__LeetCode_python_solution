class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_list = ''
        add_sum = 0
        for i in range(1, max(len(a), len(b)) + 1):
            try:
                temp_sum = int(a[-i]) + int(b[-i]) + add_sum    
            except:
                if len(a) > len(b):
                    temp_sum = int(a[-i]) + add_sum
                else:
                    temp_sum = int(b[-i]) + add_sum
            if temp_sum < 2:
                add_sum = 0
            else:
                add_sum = 1
            sum_list = str(temp_sum % 2) + sum_list
        if add_sum != 0:
            sum_list = str(add_sum) + sum_list
        return sum_list
