#Runtime: 24 ms, faster than 94.83% of Python3 online submissions for Middle of the Linked List.
#Memory Usage: 14.2 MB, less than 73.90% of Python3 online submissions for Middle of the Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dumb = head
        count = 0
        while dumb:
            count += 1
            dumb = dumb.next
        for i in range(count//2):
            head = head.next
        return head
