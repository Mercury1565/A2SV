# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(root1 , root2):
            if not root1 and not root2:
                return

            val1 = root1.val if root1 else 0
            val2 = root2.val if root2 else 0
            
            node = TreeNode(val1 + val2)

            if root1 and root2:
                node.left = merge(root1.left , root2.left)
                node.right = merge(root1.right , root2.right)
            elif root1:
                node.left = merge(root1.left , None)
                node.right = merge(root1.right , None)
            elif root2:
                node.left = merge(None , root2.left)
                node.right = merge(None , root2.right)

            return node

        return merge(root1 , root2)

