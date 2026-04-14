# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pq = [p]
        qq = [q]
        while pq and qq:
            cp = pq.pop(0)
            cq = qq.pop(0)

            if not cp and cq:
                return False
            
            if not cq and cp:
                return False
            
            if not (cp and cq):
                continue

            if not (cp.val == cq.val):
                return False
            
            pq.append(cp.left)
            pq.append(cp.right)

            qq.append(cq.left)
            qq.append(cq.right)
            
        return True