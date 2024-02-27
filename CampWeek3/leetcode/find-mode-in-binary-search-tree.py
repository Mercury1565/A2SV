# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)
        def traverse(root):
            if not root:
                return 

            traverse(root.left)
            traverse(root.right)
            dic[root.val] += 1

        traverse(root)

        max_freq = 0
        for key in dic:
            max_freq = max(max_freq , dic[key])

        output = []
        for key in dic:
            if dic[key] == max_freq:
                output.append(key)

        return output

        