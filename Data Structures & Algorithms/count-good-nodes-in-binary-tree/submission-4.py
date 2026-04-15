# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = [(root, root.val)]
        st = []
        while q:
            curr, val = q.pop(0)
            if not curr:
                continue

            if not st:
                st.append(curr.val)
            else:
                if val <= curr.val:
                    st.append(curr.val)
            
            val = max(val, curr.val)

            q.append((curr.left, val))
            q.append((curr.right, val))
        
        print(st)
        return len(st)