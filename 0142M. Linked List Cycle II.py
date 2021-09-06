#Runtime: 180 ms, faster than 5.01% of Python3 online submissions for Linked List Cycle II.
#Memory Usage: 17 MB, less than 95.45% of Python3 online submissions for Linked List Cycle II.
  
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        fast = head.next
        ind = slow = head
        cand = []
        while fast != slow:
            try:
                fast = fast.next.next
                slow = slow.next
            except:
                return None
        while slow not in cand:
            cand.append(slow)
            slow = slow.next
        while ind not in cand:
            ind = ind.next
        return ind


#Runtime: 984 ms, faster than 5.01% of Python3 online submissions for Linked List Cycle II.
#Memory Usage: 17.2 MB, less than 55.16% of Python3 online submissions for Linked List Cycle II.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        fast = head.next.next
        slow = head.next
        ind = head
        while fast != slow:
            try:
                fast = fast.next.next
                slow = slow.next
            except:
                return None
        while ind != slow:
            slow = slow.next
            while slow != fast:
                if ind == slow:
                    return ind
                else:
                    slow = slow.next
            ind = ind.next
        return ind
