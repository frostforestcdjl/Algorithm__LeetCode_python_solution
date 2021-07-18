#Runtime: 24 ms, faster than 95.17% of Python3 online submissions for Student Attendance Record I.
#Memory Usage: 14.2 MB, less than 72.02% of Python3 online submissions for Student Attendance Record I.

class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") > 1:
            return False
        if s.count("LLL") > 0:
            return False
        return True
