class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seeker = 0
        place_holder = 0

        while seeker < len(nums):
            if nums[seeker] != 0:
                nums[seeker] , nums[place_holder] = nums[place_holder] , nums[seeker]
                place_holder += 1
            seeker += 1 
                


        