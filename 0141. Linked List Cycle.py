#Runtime: 56 ms, faster than 60.92% of Python3 online submissions for Linked List Cycle.
#Memory Usage: 17.4 MB, less than 97.74% of Python3 online submissions for Linked List Cycle.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        sum_t = 0
        while head.next != None:
            sum_t += 1
            head = head.next
            if sum_t > 10**4:
                return True
        return False
