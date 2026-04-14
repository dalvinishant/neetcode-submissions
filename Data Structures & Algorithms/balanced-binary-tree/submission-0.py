# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        self.treeHeight(root)
        return self.res
    
    def treeHeight(self, root):
        if not root:
            return 0
        
        left = self.treeHeight(root.left)
        right = self.treeHeight(root.right)

        print(root.val, left, right, self.res)
        if abs(left - right) <= 1:
            self.res = self.res and True
        else:
            self.res = False
        
        return 1 + max(left, right)