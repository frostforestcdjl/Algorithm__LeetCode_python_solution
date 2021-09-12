#untime: 55 ms, faster than 7.27% of Python3 online submissions for Fraction to Recurring Decimal.
#Memory Usage: 14.2 MB, less than 96.71% of Python3 online submissions for Fraction to Recurring Decimal.
  
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        ans = ''
        if numerator * denominator < 0:
            ans += '-'
            numerator, denominator = abs(numerator), abs(denominator)
        rem = numerator%denominator
        ans += str((numerator - rem)//denominator)
        if rem == 0:
            return ans
        r_save = [str(rem)]
        dig_save = []
        recur = ""
        while rem != 0:
            new_n = rem*10
            rem = new_n%denominator
            dig = str((new_n - rem)//denominator)
            if str(rem) in r_save:
                dig_save.append(dig)
                i = r_save.index(str(rem))
                recur = "".join(dig_save[:i]) + "(" + "".join(dig_save[i:]) + ")"
                break
            else:
                dig_save.append(dig)
                r_save.append(str(rem))
        if not recur:
            recur = "".join(dig_save)
        return ans + "." + recur
