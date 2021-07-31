#Runtime: 148 ms, faster than 98.40% of Python3 online submissions for Intersection of Two Linked Lists.
#Memory Usage: 29.8 MB, less than 15.38% of Python3 online submissions for Intersection of Two Linked Lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == headB:
            return headA
        list_A = set()
        while headA:
            list_A.add(headA)
            headA = headA.next
        while headB:
            if headB in list_A:
                return headB
            headB = headB.next
        return None
