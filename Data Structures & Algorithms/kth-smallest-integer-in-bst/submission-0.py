# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        c = root
        i = 0
        while c or st:
            if c:
                st.append(c)
                c = c.left
            else:
                c = st.pop()
                i += 1
                if k == i:
                    return c.val
                c = c.right
