#Runtime: 28 ms, faster than 98.22% of Python3 online submissions for Merge Two Sorted Lists.
#Memory Usage: 14.2 MB, less than 85.43% of Python3 online submissions for Merge Two Sorted Lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        r_l = ListNode()
        temp = r_l
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        while l1 != None and l2 != None:
            if l2.val < l1.val:
                temp.next = l2
                l2 = l2.next
                temp = temp.next
            else:
                temp.next = l1
                l1 = l1.next
                temp = temp.next
            if l1 == None:
                temp.next = l2
                break
            if l2 == None:
                temp.next = l1
                break
        return r_l.next
