#Runtime: 40 ms, faster than 25.11% of Python3 online submissions for Binary Watch.
#Memory Usage: 14 MB, less than 99.41% of Python3 online submissions for Binary Watch.

#Runtime: 28 ms, faster than 90.75% of Python3 online submissions for Binary Watch.
#Memory Usage: 14.3 MB, less than 32.60% of Python3 online submissions for Binary Watch.

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8:
            return []
        if turnedOn == 0:
            return ["0:00"]
        def hour(hr_n):
            if hr_n == 0:
                return ["0:"]
            if hr_n == 1:
                return ["1:", "2:", "4:", "8:"]
            if hr_n == 2:
                return ["3:", "5:", "9:", "6:", "10:"]
            if hr_n == 3:
                return ["7:", "11:"]
            return []
        def minute(min_n):
            if min_n == 0:
                return ["00"]
            if min_n == 1:
                return ["01", "02", "04", "08", "16", "32"]
            if min_n == 2:
                return ["03", "05", "09", "17", "33", "06", "10", "18", "34", "12", "20", "36", "24", "40", "48"]
            if min_n == 3:
                return ["07", "11", "19", "35", "13", "21", "37", "25", "41", "49", "14", "22", "38", "26", "42", "50", "28", "44", "52", "56"]
            if min_n == 4:
                return ["15", "23", "39", "27", "43", "51", "29", "45", "53", "57", "30", "46", "54", "58"]
            if min_n == 5:
                return ["31", "47", "55", "59"]
            return []
        possible = []
        for i in range(min(4, turnedOn + 1)):
            min_list = minute(turnedOn - i)
            hr_list = hour(i)
            for j in hr_list:
                for k in min_list:
                    possible.append(j+k)
        return possible
