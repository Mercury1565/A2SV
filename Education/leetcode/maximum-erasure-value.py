class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        window = set()
        score = 0
        left = 0

        for right in range(len(nums)):
            while nums[right] in window:
                window.remove(nums[left])
                left += 1

            window.add(nums[right])
            score = max(score , sum(window))
            
        return score

        