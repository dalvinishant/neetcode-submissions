"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        cloned_node = self.clone(visited, node)
        return cloned_node

    def clone(self, v, n):
        if not n or (n and n.val in v):
            return
        new_node = Node(n.val, [])
        v.update({n.val: new_node})
        for neighbor in n.neighbors:
            if neighbor.val in v:
                new_node.neighbors.append(v[neighbor.val])
            else:
                new_node.neighbors.append(self.clone(v, neighbor))
        return new_node
