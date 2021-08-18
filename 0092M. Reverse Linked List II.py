#Runtime: 24 ms, faster than 95.87% of Python3 online submissions for Reverse Linked List II.
#Memory Usage: 14.4 MB, less than 71.06% of Python3 online submissions for Reverse Linked List II.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        r_head = r_mid = ListNode(0)
        r_head.next = r_mid.next = head
        r_list = []
        for i in range(left-1):
            r_mid = r_mid.next
        rev = r_mid.next
        for i in range(right-left+1):
            r_list.append(rev.val)
            rev = rev.next
        for i in range(right-left+1):
            r_mid.next = ListNode(r_list[~i])
            r_mid = r_mid.next
        r_mid.next = rev
        return r_head.next
