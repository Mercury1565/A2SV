class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def permutation(path):
            if len(path) == len(nums):
                result.append(path[:])
                print
                return
            
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                    
                path.append(nums[i])

                permutation(path)
                path.pop()

        permutation([])

        return result