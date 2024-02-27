class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def fun(curr , path):
            if len(path) == len(nums):
                return
        
            for choice in range(curr , len(nums)):
                path.append(nums[choice])
                ans.append(path[:])

                fun(choice + 1 , path)
                path.pop()

        ans = []
        fun(0 , [])
        return [[]] + ans    

        