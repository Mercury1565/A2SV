class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ssum = 0
        left = 0
        result = len(nums) + 1

        for right in range(len(nums)):
            ssum += nums[right]

            if ssum >= target:
                while ssum >= target:
                    result = min(result , right - left + 1)
                    ssum -= nums[left]
                    left += 1
    
        return result if result <= len(nums) else 0

