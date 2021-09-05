#Runtime: 24 ms, faster than 94.59% of Python3 online submissions for Defanging an IP Address.
#Memory Usage: 14.2 MB, less than 65.16% of Python3 online submissions for Defanging an IP Address.

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
