class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        val = nums[0]
        k = 1
        for i in nums:
            if i != val:
                val = i
                nums[k] = val
                k += 1
        return k
