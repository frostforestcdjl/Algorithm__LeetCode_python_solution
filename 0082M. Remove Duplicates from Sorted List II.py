#Runtime: 40 ms, faster than 71.51% of Python3 online submissions for Remove Duplicates from Sorted List II.
#Memory Usage: 14.2 MB, less than 83.12% of Python3 online submissions for Remove Duplicates from Sorted List II.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        re = ListNode(0)
        re.next = head
        dumb = re
        try:
            while dumb.next.next:
                if dumb.next.val == dumb.next.next.val:
                    val = dumb.next.val
                    while dumb.next.val == val:
                        dumb.next = dumb.next.next
                else:
                    dumb = dumb.next
        except:
            pass
        return re.next
