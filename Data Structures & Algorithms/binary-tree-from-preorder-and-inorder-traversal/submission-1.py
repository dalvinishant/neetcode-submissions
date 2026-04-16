# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_i = 0
        self.ino_map = {val: i for i, val in enumerate(inorder)}
        return self.createTree(0, len(preorder) - 1)
    
    def createTree(self, left, right):

        if left > right:
            return None
        
        root = TreeNode(preorder[self.pre_i])
        self.pre_i += 1
        mid = self.ino_map[root.val]
        root.left  = self.createTree(left, mid - 1)
        root.right = self.createTree(mid + 1, right)
        return root        
        
            
            
