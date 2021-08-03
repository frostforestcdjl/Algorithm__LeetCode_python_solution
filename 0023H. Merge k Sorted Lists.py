#Runtime: 756 ms, faster than 13.48% of Python3 online submissions for Merge k Sorted Lists.
#Memory Usage: 17.7 MB, less than 92.60% of Python3 online submissions for Merge k Sorted Lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        while None in lists:
            lists.pop(lists.index(None))
        if not lists:
            return None
        if len(lists) < 2:
            return lists[0]
        min_l = ListNode(0)
        head = min_l
        min_val = lists[0].val
        cand = lists
        
        cand_val = []
        for i in cand:
            cand_val.append(i.val)
        while cand_val:
            min_index = cand_val.index(min(cand_val))
            head.next = cand[min_index]
            if cand[min_index].next != None:
                cand[min_index] = cand[min_index].next
                cand_val[min_index] = cand[min_index].val
            else:
                cand.pop(min_index)
                cand_val.pop(min_index)
            head = head.next
        
        return min_l.next
