# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_node = root.left
        right_node = root.right

        def mirror_check(root_1 , root_2):
            if not root_1 and not root_2:
                return True
            elif root_1 and not root_2:
                return False
            elif root_2 and not root_1:
                return False
            
            if root_1.val != root_2.val:
                return False
            
            bool_1 = mirror_check(root_1.left , root_2.right)
            bool_2 = mirror_check(root_1.right , root_2.left)

            return bool_1 and bool_2

        return mirror_check(left_node , right_node)

        

        