# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.res = root.val
        self.dfs(root)
        return self.res
    
    def dfs(self, root):

        if not root:
            return 0
        
        left_sub = self.dfs(root.left)
        right_sub = self.dfs(root.right)

        left_sub = max(left_sub, 0)
        right_sub = max(right_sub, 0)

        self.res = max(self.res, left_sub + root.val + right_sub)
        return root.val + max(left_sub, right_sub)