#Runtime: 40 ms, faster than 81.67% of Python3 online submissions for Remove Duplicates from Sorted List.
#Memory Usage: 14 MB, less than 94.20% of Python3 online submissions for Remove Duplicates from Sorted List.
  
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        try:
            output = head
            while head.next != None:
                if head.next.val == head.val:
                    temp = head.next.next
                    head.next = temp
                else:
                    head = head.next
            return output
        except:
            return head
