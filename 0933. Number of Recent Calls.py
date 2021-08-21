#Runtime: 276 ms, faster than 87.87% of Python3 online submissions for Number of Recent Calls.
#Memory Usage: 18.9 MB, less than 70.27% of Python3 online submissions for Number of Recent Calls.

class RecentCounter:

    def __init__(self):
        self.plist = []

    def ping(self, t: int) -> int:
        self.plist.append(t)
        while self.plist[0] < t - 3000:
            self.plist.pop(0)
        return len(self.plist)
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
