class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        val = nums[0]
        k = 1
        for n in nums:
            if n != val:
                val = n
                nums[k] = val
                k += 1
      
        return k