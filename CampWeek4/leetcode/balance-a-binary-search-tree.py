# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        traversal = []

        def inOrd_traverse(root):
            if not root:
                return root
            
            inOrd_traverse(root.left)
            traversal.append(root.val)
            inOrd_traverse(root.right)

        inOrd_traverse(root)

        def build(arr):
            if not arr:
                return 

            mid = len(arr) // 2

            left = arr[ : mid]
            right = arr[mid + 1 : ]

            node = TreeNode(arr[mid])
            node.left = build(left)
            node.right = build(right)

            return node

        return build(traversal)


        