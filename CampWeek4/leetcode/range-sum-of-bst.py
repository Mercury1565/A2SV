# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        if not root:
            return 0        

        if root.val <= high and root.val >= low:

            left = self.rangeSumBST(root.left , low , high)
            right = self.rangeSumBST(root.right , low , high) 

            return root.val + left + right
        if root.val < low:
            return self.rangeSumBST(root.right , low , high)
        if root.val > high:
            return self.rangeSumBST(root.left , low , high)


      