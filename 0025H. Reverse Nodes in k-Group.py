#Runtime: 52 ms, faster than 48.94% of Python3 online submissions for Reverse Nodes in k-Group.
#Memory Usage: 15.7 MB, less than 9.37% of Python3 online submissions for Reverse Nodes in k-Group.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        val_list = []
        re_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        while len(val_list) >= k:
            re_list += val_list[k-1::-1]
            val_list = val_list[k:]
        if len(val_list) != 0:
            re_list += val_list
        re = temp = ListNode(0)
        for i in re_list:
            temp.next = ListNode(i)
            temp = temp.next
        return re.next
