class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def subset(curr , path):
            if len(path) == len(nums):
                return 

            for i in range(curr , len(nums)):
                path.append(nums[i])

                sorted_path = sorted(path)
                if sorted_path not in result:
                    result.append(sorted_path)

                subset(i + 1 , path)
                path.pop()
        result = []
        subset(0 , [])

        return [[]] + result
        