class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0

        fac = 1
        for i in range(n):
            fac = fac * (i+1)
        y = list(str(fac))
        while y[-(count+1)] == '0':
            count += 1
        return count
