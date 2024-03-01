# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level = [(root , 1)]
        if not root:
            return []
        ans = 1
        while level:
            next_level = []
            temp = []
            for node,val in level:
                if node.left:
                    next_level.append((node.left , val * 2))
                    temp.append(val * 2)
                if node.right:
                    next_level.append((node.right , (val * 2) + 1))
                    temp.append((val * 2) + 1)

            if next_level:
                ans = max(ans , temp[-1] - temp[0] + 1)
            level = next_level
            
        return ans

        