#Runtime: 28 ms, faster than 89.39% of Python3 online submissions for Cousins in Binary Tree.
#Memory Usage: 14.1 MB, less than 88.60% of Python3 online submissions for Cousins in Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        stack = [[root,0]]
        depth = 0
        x_d = -1
        y_d = -1
        while stack:
            try:
                if stack[0][0].left.val in [x, y] and stack[0][0].right.val in [x, y]:
                    return False
            except:
                pass
            node = stack.pop(0)
            if node[0].val == x:
                x_d = node[1]
            if node[0].val == y:
                y_d = node[1]
            if node[0].left:
                stack.append([node[0].left, node[1]+1])
            if node[0].right:
                stack.append([node[0].right, node[1]+1])
            if x_d > 0 and x_d == y_d:
                return True
        return False
