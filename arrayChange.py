class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {}

        for index , num in enumerate(nums):
            d[num] = index
        
        for source , destin in operations:
            index = d[source]
            nums[index] = destin
            d[destin] = index          

        return nums
        
