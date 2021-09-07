#Runtime: 44 ms, faster than 98.66% of Python3 online submissions for Insertion Sort List.
#Memory Usage: 17.4 MB, less than 9.79% of Python3 online submissions for Insertion Sort List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cand = []
        while head:
            cand.append(head.val)
            head = head.next
        cand.sort(reverse = True)
        re = temp = ListNode(0)
        while cand:
            temp.next = ListNode(cand.pop())
            temp = temp.next
        return re.next


#Runtime: 1984 ms, faster than 22.96% of Python3 online submissions for Insertion Sort List.
#Memory Usage: 17.2 MB, less than 11.48% of Python3 online submissions for Insertion Sort List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        run = head
        re = ListNode(run.val)
        while run.next:
            run = run.next
            sing = ListNode(run.val)
            temp = re
            if sing.val < temp.val:
                sing.next = temp
                re = sing
            else:
                while temp.next and temp.next.val < sing.val:
                    temp = temp.next
                sing.next = temp.next
                temp.next = sing
        return re
