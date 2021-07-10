#Runtime: 24 ms, faster than 94.74% of Python3 online submissions for First Bad Version.
#Memory Usage: 14.1 MB, less than 72.50% of Python3 online submissions for First Bad Version.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        head = 1
        tail = n
        
        while abs(tail - head) > 1:
            guess_n = round((head + tail)/2 + 0.1)
            if isBadVersion(guess_n) == True:
                tail = guess_n
            else:            
                head = guess_n
        if head == tail:
            return head
        if isBadVersion(head) == True:
            return head
        return tail
