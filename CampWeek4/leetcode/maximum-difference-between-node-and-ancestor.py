# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_min = [0 , inf]
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = 0
        def max_diff(root):
            nonlocal result


            if not root.left and not root.right:
                return root.val , root.val

            elif not root.right:
                temp = max_diff(root.left)
                maxx = max(root.left.val , temp[0])
                minn = min(root.left.val , temp[1])

            elif not root.left:
                temp = max_diff(root.right)
                maxx = max(root.right.val , temp[0])
                minn = min(root.right.val , temp[1])

            else:
                right = max_diff(root.right)
                left = max_diff(root.left)

                maxx = max(root.right.val , root.left.val , right[0] , left[0])
                minn = min(root.right.val , root.left.val , right[1] , left[1])


            diff_with_max = abs(root.val - maxx)
            diff_with_min = abs(root.val - minn)

            result = max(result , diff_with_max , diff_with_min)

            return maxx , minn

        max_diff(root)

        return result







