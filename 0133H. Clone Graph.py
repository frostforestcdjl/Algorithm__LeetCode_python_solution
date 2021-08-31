#Runtime: 36 ms, faster than 79.84% of Python3 online submissions for Clone Graph.
#Memory Usage: 14.5 MB, less than 83.37% of Python3 online submissions for Clone Graph.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        stack = [node]
        record = {node:Node(node.val)}
        while stack:
            c_node = stack.pop(0)
            cp_node = record[c_node]
            if not cp_node.neighbors:
                cp_node.neighbors = []
            for i in c_node.neighbors:
                if i not in record:
                    cand = Node(i.val)
                    cp_node.neighbors += [cand]
                    record[i] = cand
                    stack.append(i)
                else:
                    cp_node.neighbors.append(record[i])
        return record[node]
