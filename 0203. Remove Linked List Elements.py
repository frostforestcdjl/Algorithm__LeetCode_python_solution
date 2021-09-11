#Runtime: 65 ms, faster than 74.43% of Python3 online submissions for Remove Linked List Elements.
#Memory Usage: 17.1 MB, less than 66.78% of Python3 online submissions for Remove Linked List Elements.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        test = re = ListNode(0)
        test.next = head
        while test and test.next:
            while test.next and test.next.val == val:
                test.next = test.next.next
            test = test.next
        return re.next
