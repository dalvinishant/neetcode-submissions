# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = [root]
        rightSide = []
        while q:
            level = []
            level_size = len(q)
            i = 0
            while i < level_size:
                curr = q.pop(0)
                i += 1

                if not curr:
                    continue
                
                level.append(curr.val)

                q.append(curr.left)
                q.append(curr.right)
                # print(curr.val, level)

            if level:
                rightSide.append(level[-1])
        
        return rightSide