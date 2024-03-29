# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:  
        arr = []

        def in_order_traverse(root):
            if not root:
                return 

            in_order_traverse(root.left)
            arr.append(root.val)
            in_order_traverse(root.right)
        
        in_order_traverse(root)

        for i in range(1 , len(arr)):
            if arr[i] <= arr[i - 1]:
                return False

        return True


 
        