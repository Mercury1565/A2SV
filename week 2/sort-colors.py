class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for j in range(0 , len(nums)):
            idx = j
            for y in range(j , len(nums)):
                if nums[y] < nums[idx]:
                    idx = y
            nums[idx] , nums[j] = nums[j] , nums[idx]
        