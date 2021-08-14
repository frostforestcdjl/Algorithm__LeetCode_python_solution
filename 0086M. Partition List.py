#Runtime: 28 ms, faster than 95.05% of Python3 online submissions for Partition List.
#Memory Usage: 14.2 MB, less than 84.72% of Python3 online submissions for Partition List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = resmall = ListNode(0)
        big = rebig = ListNode(0)
        while head:
            if head.val >= x:
                big.next = head
                big = big.next
            else:
                small.next = head
                small = small.next
            head = head.next
        if big.next:
            big.next = None
        small.next = rebig.next
        return resmall.next
