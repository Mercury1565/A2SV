# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def search_ancestor(root , p  , q):
            if not root:
                return

            print(root.val , p.val , q.val)
            if p.val <= root.val <= q.val:
                return root
            elif root.val < p.val:
                return search_ancestor(root.right , p , q)
            elif root.val > q.val:
                return search_ancestor(root.left , p , q)

        if p.val < q.val:
            left , right = p , q
        elif q.val < p.val:
            left , right = q , p

        return search_ancestor(root , left , right)
            