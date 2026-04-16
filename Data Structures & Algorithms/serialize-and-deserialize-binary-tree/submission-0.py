# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.serialized = []
        self.serializeTree(root)
        return ",".join(self.serialized)

    def serializeTree(self, root):

        if not root:
            self.serialized.append("")
            return
        
        self.serialized.append(str(root.val))
        self.serializeTree(root.left)
        self.serializeTree(root.right)
 

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.pre_i = 0
        print(data.split(","))
        root = self.createTree(data.split(","))
        return root
    
    def createTree(self, preorder):

        if not preorder[self.pre_i]:
            self.pre_i +=1 
            return None
        
        root = TreeNode(int(preorder[self.pre_i]))
        self.pre_i += 1
        root.left = self.createTree(preorder)
        root.right = self.createTree(preorder)

        return root


