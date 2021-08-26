#Runtime: 28 ms, faster than 92.15% of Python3 online submissions for Remove Nth Node From End of List.
#Memory Usage: 14.2 MB, less than 76.85% of Python3 online submissions for Remove Nth Node From End of List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        fast = slow = head
        for i in range(n-1):
            fast = fast.next
        if not fast.next:
            return head.next
        while fast.next.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
