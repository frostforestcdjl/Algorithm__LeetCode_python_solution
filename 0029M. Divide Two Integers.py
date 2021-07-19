#Runtime: 24 ms, faster than 98.12% of Python3 online submissions for Divide Two Integers.
#Memory Usage: 14.3 MB, less than 20.50% of Python3 online submissions for Divide Two Integers.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend == -2147483648:
                return 2147483647
            return 0 - dividend
        if dividend > 0 and divisor > 0:
            final_i = 0
            while dividend >= divisor:
                temp_divisor = 0 + divisor
                temp_i = 0.5
                while dividend >= temp_divisor:
                    temp_i = temp_i + temp_i
                    dividend -= temp_divisor
                    temp_divisor = temp_divisor + temp_divisor
                    final_i += temp_i
            return int(final_i)
            
        if dividend < 0 and divisor < 0:
            final_i = 0
            while dividend <= divisor:
                temp_divisor = 0 + divisor
                temp_i = 0.5
                while dividend <= temp_divisor:
                    temp_i = temp_i + temp_i
                    dividend -= temp_divisor
                    temp_divisor = temp_divisor + temp_divisor
                    final_i += temp_i
            return int(final_i)
        
        if dividend > 0 and divisor < 0:
            final_i = 0
            while (dividend + divisor) >= 0:
                temp_divisor = 0 + divisor
                temp_i = -0.5
                while (dividend + temp_divisor) >= 0:
                    temp_i = temp_i + temp_i
                    dividend += temp_divisor
                    temp_divisor = temp_divisor + temp_divisor
                    final_i += temp_i
            return int(final_i)
                
        if dividend < 0 and divisor > 0:
            final_i = 0
            while (dividend + divisor) <= 0:
                temp_divisor = 0 + divisor
                temp_i = -0.5
                while (dividend + temp_divisor) <= 0:
                    temp_i = temp_i + temp_i
                    dividend += temp_divisor
                    temp_divisor = temp_divisor + temp_divisor
                    final_i += temp_i
            return int(final_i)
