class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        result = 0

        for n in nums:
            if n != 1:
                result = max(result , count)
                count = 0
                continue
            count += 1
        
        return max(result , count)
        