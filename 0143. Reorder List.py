#Runtime: 88 ms, faster than 86.24% of Python3 online submissions for Reorder List.
#Memory Usage: 23.3 MB, less than 49.86% of Python3 online submissions for Reorder List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        re = fast = slow = head
        while fast.next and fast.next.next:
            fast, slow = fast.next.next, slow.next
            
        last, slow.next, rev_last = slow.next, None, []

        while last:
            rev_last.append(last)
            last = last.next
        while rev_last:
            backup, re.next = re.next, rev_last.pop()
            re.next.next = backup
            re = re.next.next
