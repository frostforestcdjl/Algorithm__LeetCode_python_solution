#Runtime: 68 ms, faster than 72.46% of Python3 online submissions for Day of the Year.
#Memory Usage: 14.1 MB, less than 83.07% of Python3 online submissions for Day of the Year.

class Solution:
    def dayOfYear(self, date: str) -> int:
        count = 0
        bm = [1, 3, 5, 7, 8, 10, 12]
        sm = [4, 6, 9, 11]
        y, m, d = int(date[:4]), int(date[5:7])-1, int(date[8:])
        if y%4 == 0 and (y%100 != 0 or y%1000 == 0) and m >= 2:
            count += 1
        if m == 0:
            pass
        elif m in bm:
            count += 30*m + bm.index(m)+1
        elif m in sm:
            count += 30*m + bm.index(m-1)+1
        else:
            count += 59
        if m > 2:
            count -= 2
        count += d
        return count
