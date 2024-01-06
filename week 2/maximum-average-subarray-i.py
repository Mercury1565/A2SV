class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_avg = window_sum / k

        for i in range(k , len(nums)):
            window_sum -= nums[i - k]
            window_sum += nums[i]
            max_avg = max(max_avg , window_sum / k)

        return max_avg
        
        