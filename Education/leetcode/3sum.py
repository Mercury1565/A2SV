class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = set()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue   
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    arr.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
           
        return arr