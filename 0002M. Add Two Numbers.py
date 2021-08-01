#Runtime: 60 ms, faster than 96.77% of Python3 online submissions for Add Two Numbers.
#Memory Usage: 14.2 MB, less than 90.62% of Python3 online submissions for Add Two Numbers.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        add = 0
        out = l1
        
        while l1.next and l2.next:
            temp_sum = l1.val + l2.val + add
            l1.val = temp_sum%10
            add = temp_sum//10
            l1 = l1.next
            l2 = l2.next
        temp_sum = l1.val + l2.val + add
        l1.val = temp_sum%10
        add = temp_sum//10
        if l1.next == None and l2.next == None and add != 0:
            l1.next = ListNode(add)
            return out
        if l1.next == None and l2.next != None:
            l1.next, l2.next = l2.next, l1.next
        l1 = l1.next
                
        while l1:
            temp_sum = l1.val + add
            l1.val = temp_sum%10
            add = temp_sum//10
            if l1.next == None and add != 0:
                l1.next = ListNode(add)
                return out
                l1 = l1.next
            l1 = l1.next
        return out
