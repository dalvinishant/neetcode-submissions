# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(0, root)
    
    def depth(self, d, root):
        if not root:
            return d
        
        return max(self.depth(d+1, root.left), self.depth(d+1, root.right))