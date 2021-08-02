#Runtime: 28 ms, faster than 97.95% of Python3 online submissions for Rotate List.
#Memory Usage: 14 MB, less than 99.63% of Python3 online submissions for Rotate List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        test_length = head
        total_length = 0
        while test_length:
            total_length += 1
            test_length = test_length.next
        new_head_n = k%total_length
        if new_head_n == 0:
            return head
        new_tail_n = total_length - new_head_n
        
        new_tail = head
        for i in range(new_tail_n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = ListNode().next
        
        part_head = new_head
        for i in range(new_head_n - 1):
            part_head = part_head.next
        part_head.next = head
        
        return new_head
