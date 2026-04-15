# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = [root]
        lca = root
        pv, qv = False, False

        while queue and not pv:
            curr = queue[-1]

            if not curr:
                continue

            if p.val == curr.val:
                pv = True
                queue.append(curr)
            elif p.val < curr.val:
                queue.append(curr.left)
            else:
                queue.append(curr.right)

        while queue and not qv: 
            curr = queue.pop()
            if not curr:
                continue
            
            lca = curr
            print("===", curr.val)
            while curr:
                print(curr.val)
                if q.val == curr.val:
                    qv = True
                    break
                if q.val < curr.val:
                    curr = curr.left
                else:
                    curr = curr.right

        return lca

