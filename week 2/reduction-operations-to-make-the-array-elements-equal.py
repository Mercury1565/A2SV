class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        dic = {}
        count = 0
    
        nums.sort()

        idx = 0
        for i in range(len(nums)):
            if i != 0 and nums[i] != nums[i - 1]:
                idx += 1
            dic[nums[i]] = idx

        for n in nums:
            count += dic[n]

        return count
        