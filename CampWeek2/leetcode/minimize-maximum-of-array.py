class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maxx = nums[0]
        total = nums[0]
        
        if maxx == max(nums):
            return maxx

        for i in range(1 , len(nums)):
            total += nums[i]
            maxx = max(math.ceil(total / (i + 1)) , maxx) 

        return maxx      