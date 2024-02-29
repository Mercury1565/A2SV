class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        l , r = 0 , 0
        numDistinct = len(set(nums))
        count = 0
        counter = Counter()

        while r < len(nums):
            counter[nums[r]] += 1
            while len(counter) == numDistinct:
                counter[nums[l]] -= 1
                if counter[nums[l]] == 0:
                    del counter[nums[l]]
                l += 1
                count += len(nums) - r
            r += 1
        return count


       