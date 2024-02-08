class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ssum = 0
        result = nums[0]

        for r in range(len(nums)):
            ssum += nums[r]
            result = max(result , ssum)

            if ssum < 0:
                ssum = 0
                

        return result


        