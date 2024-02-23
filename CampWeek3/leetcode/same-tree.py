# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def compare(p , q):
            if p == None and q == None:
                return True

            if p and q and p.val == q.val:
                x = compare(p.left , q.left)
                y = compare(p.right , q.right)
                return x and y

        return compare(p , q) 
