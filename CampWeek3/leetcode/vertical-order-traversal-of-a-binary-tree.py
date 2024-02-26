# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        def fun(root , row , col):
            if not root:
                return 
            dic[col].append((row , root.val))
            fun(root.left , row + 1 , col - 1) 
            fun(root.right , row + 1 , col + 1)

        fun(root , 0 , 0)
  
        min_idx = min(dic.keys())
        result = [0] * len(dic)
     
        for key in dic:
            temp = []
            arr = sorted(dic[key])
            print(arr)
            for pair in arr:
                temp.append(pair[1])
            result[key - min_idx] = temp

        return result