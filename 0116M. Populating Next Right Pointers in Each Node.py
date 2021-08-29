#Runtime: 60 ms, faster than 80.85% of Python3 online submissions for Populating Next Right Pointers in Each Node.
#Memory Usage: 15.6 MB, less than 91.22% of Python3 online submissions for Populating Next Right Pointers in Each Node.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        stack = [root]
        level = 0
        count = 0
        while stack:
            node = stack.pop(0)
            if stack:
                node.next = stack[0]
            count += 1
            if count == 2**level:
                node.next = None
                count = 0
                level += 1
            if node.left:
                stack.append(node.left)
                stack.append(node.right)
        return root
