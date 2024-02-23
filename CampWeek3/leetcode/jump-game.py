class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #1 3 0 0 2 0 9
        #0 1 2 3 4 5 6
        #        *
        # p = len(nums) - 1
        good_ptr = len(nums) - 1

        for i in range(len(nums) - 2 , -1 , -1):
            if i + nums[i] >= good_ptr:
                good_ptr = i

        return good_ptr == 0


