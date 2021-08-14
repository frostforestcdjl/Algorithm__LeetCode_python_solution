#Runtime: 95 ms, faster than 5.59% of Python3 online submissions for Symmetric Tree.
#Memory Usage: 14.6 MB, less than 19.57% of Python3 online submissions for Symmetric Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        print(root)
        if (root.left == None) != (root.right == None):
            return False
        if root.left == None:
            return True
        stack = [[root.left, root.right]]
        i = 0
        while i < len(stack):
            if stack[i][0].val != stack[i][1].val:
                return False
            else:
                if (stack[i][0].left == None) != (stack[i][1].right == None):
                    return False
                if (stack[i][0].right == None) != (stack[i][1].left == None):
                    return False
                if stack[i][0].left and stack[i][1].right:
                    stack.append([stack[i][0].left, stack[i][1].right])
                if stack[i][0].right and stack[i][1].left:
                    stack.append([stack[i][0].right, stack[i][1].left])
            i += 1
        return True
