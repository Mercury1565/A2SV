# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def fun(root , ssum):
            nonlocal max_sum

            if not root:
                max_sum = max(max_sum , 0)
                return 0 , True , float('inf') , float('-inf')

            left = fun(root.left , ssum)
            right = fun(root.right , ssum)

            if left[1] and right[1] and left[3] < root.val < right[2]:
                curr_sum = left[0] + right[0] + root.val
                max_sum = max(max_sum , curr_sum)

                new_max_to_right = min(root.val , left[2])
                new_min_to_left = max(root.val , right[3])

                return curr_sum , True , new_max_to_right , new_min_to_left 

            #return ssum , isBST , min_to_Left , max_to_Right
            return 0 , False , 0 , 0

        fun(root , 0)
        return max_sum
       