class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nMap = {}

        for i in range(len(nums)):
            nMap[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nMap and nMap[complement] != i:
                return [i, nMap[complement]]

        return []  
