# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def recursion(arr):
            if not arr:
                return
            
            maxx = max(arr)
            max_index = arr.index(maxx)

            node = TreeNode(maxx)
            node.left = recursion(arr[ : max_index])
            node.right = recursion(arr[max_index + 1 : ])

            return node

        return recursion(nums)




