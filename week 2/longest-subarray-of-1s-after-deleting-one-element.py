class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        left , right = 0 , 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

                if zero_count == 2:
                    max_length = max(max_length , right - left - 1)
                    zero_count -= 1
                
                    while nums[left] == 1:
                        left += 1
                    left += 1
                    
        max_length = max(max_length , right - left)
        return max_length
        