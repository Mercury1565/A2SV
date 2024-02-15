class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, prefix = 0, 0
        i = 0
        while prefix < n:
            if i < len(nums) and nums[i] <= prefix + 1:
                prefix += nums[i]
                i += 1
            else:
                prefix += (prefix + 1)
                patches += 1
        return patches



