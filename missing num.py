class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lis = list(range(len(nums)+1))
        for i in nums:
            if i in lis:
                lis.remove(i)
        return lis[0]
        
