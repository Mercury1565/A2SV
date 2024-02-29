# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = values
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def fun(node , values):
            if values:
                mid = len(values)//2

                node.val = values[mid]
                node.left = fun(TreeNode() , values[:mid])
                node.right = fun(TreeNode() , values[mid+1:])

                return node  
                
        return fun(TreeNode(),nums)
        