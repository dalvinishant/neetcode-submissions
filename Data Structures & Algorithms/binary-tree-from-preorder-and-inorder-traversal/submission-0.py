# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.ino_map = {val: i for i, val in enumerate(inorder)}
        return self.createTree(preorder, inorder)
    
    def createTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.createTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.createTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
            
            
