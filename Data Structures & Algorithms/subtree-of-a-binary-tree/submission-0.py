# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = [root]
        while q:
            curr = q.pop(0)
            
            if not curr:
                continue

            if curr.val == subRoot.val:
                res = self.isSameTree(curr, subRoot)
                if res:
                    return True
            
            q.append(curr.left)
            q.append(curr.right)
        
        return False
    
    def isSameTree(self, source, target):

        if not source and not target:
            return True
        
        if source and not target or not source and target:
            return False
        
        return source.val == target.val and self.isSameTree(source.left, target.left) and self.isSameTree(source.right, target.right)
