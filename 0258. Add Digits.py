#Runtime: 28 ms, faster than 89.51% of Python3 online submissions for Add Digits.
#Memory Usage: 14.1 MB, less than 69.72% of Python3 online submissions for Add Digits.

class Solution:
    def addDigits(self, num: int) -> int:
        num_list = list(str(num))
        while len(num_list) > 1:
            temp_sum = 0
            while len(num_list) > 0:
                temp_sum += int(num_list[0])
                num_list.pop(0)
            num_list = list(str(temp_sum))
        return int(num_list[0])
