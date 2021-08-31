#Runtime: 32 ms, faster than 87.63% of Python3 online submissions for Reverse Linked List.
#Memory Usage: 16.5 MB, less than 20.92% of Python3 online submissions for Reverse Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cand = []
        while head:
            cand.append(head.val)
            head = head.next
        cand = cand[::-1]
        dumb = re = ListNode(cand.pop(0))
        while cand:
            re.next = ListNode(cand.pop(0))
            re = re.next
        return dumb
