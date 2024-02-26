# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        def zigzag(root , level):
            if not root:
                return

            if level >= len(output):
                output.append([root.val])
            else:
                output[level].append(root.val)

            zigzag(root.left , level + 1)
            zigzag(root.right , level + 1)

        zigzag(root , 0)

        for i in range(len(output)):
            if i % 2:
                output[i] = output[i][::-1]
        return output

            

        

        