# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        st = []
        bst = []
        curr = root

        while curr or st:
            if curr:
                st.append(curr)
                curr = curr.left
            else:
                curr = st.pop()
                bst.append(curr.val)
                curr = curr.right

        if len(bst) > 1:
            i = 0
            j = 1

            while j < len(bst):
                if bst[i] >= bst[j]:
                    return False
                i += 1
                j += 1

        return True