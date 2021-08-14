#Runtime: 16 ms, faster than 99.86% of Python3 online submissions for Same Tree.
#Memory Usage: 14.4 MB, less than 31.71% of Python3 online submissions for Same Tree.

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p or not q:
            return p == q
        cand_p = []
        cand_q = []
        def go_deep(node, cand):
            cand.append(node.val)
            if not node.left and not node.right:
                return cand
            if node.left:
                cand = go_deep(node.left, cand)
            else:
                cand.append(None)
            if node.right:
                cand = go_deep(node.right, cand)
            return cand
        return go_deep(p, cand_p) == go_deep(q, cand_q)
