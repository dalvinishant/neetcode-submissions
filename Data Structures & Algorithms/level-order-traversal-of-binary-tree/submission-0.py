# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        self.bfs(levels, root)
        return levels
    
    def bfs(self, levels, node):
        if not node:
            return
        q = [node]
        while q:
            c_level = []
            i = 0
            j = 0
            size = len(q)
            c_list = []
            while i < size:
                n = q.pop(0)

                c_level.append(n.val)
                i += 1

                if n.left:
                    c_list.append(n.left)
                if n.right:
                    c_list.append(n.right)

            print(q)
            q += c_list

            levels.append(c_level.copy())
            