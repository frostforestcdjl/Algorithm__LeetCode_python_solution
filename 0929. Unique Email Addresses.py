#Runtime: 40 ms, faster than 98.84% of Python3 online submissions for Unique Email Addresses.
#Memory Usage: 14.3 MB, less than 85.02% of Python3 online submissions for Unique Email Addresses.

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        cand = set()
        for i in emails:
            back = i[i.index('@'):]
            if '+' in i:
                front = i[:i.index('+')].replace('.', '')
            else:
                front = i[:i.index('@')].replace('.', '')
            if front + back not in cand:
                cand.add(front + back)
        return len(list(cand))
